import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

DEBUG_LOG_FILE = Path(os.environ.get("MGREP_WATCH_LOG", "/tmp/mgrep-watch.log"))


def debug_log(message: str) -> None:
    try:
        DEBUG_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DEBUG_LOG_FILE, "a", encoding="utf-8") as handle:
            handle.write(f"[{stamp}] {message}\n")
    except Exception:
        pass


def read_hook_input() -> dict[str, object] | None:
    raw = sys.stdin.read()
    if not raw.strip():
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        debug_log(f"Failed to decode JSON: {exc}")
        return None


def is_pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    else:
        return True


if __name__ == "__main__":
    payload = read_hook_input()
    if payload is None:
        sys.exit(0)

    session_id = payload.get("sessionId") or payload.get("session_id")
    pid_file = f"/tmp/mgrep-watch-pid-{session_id}.txt"

    if os.path.exists(pid_file):
        try:
            existing_pid = int(Path(pid_file).read_text(encoding="utf-8").strip())
        except Exception:
            existing_pid = None

        if existing_pid and is_pid_alive(existing_pid):
            debug_log(f"mgrep watch already running for session {session_id}: {existing_pid}")
            sys.exit(0)

        # stale pid file
        try:
            Path(pid_file).unlink(missing_ok=True)
        except Exception:
            pass

    process = subprocess.Popen(
        ["mgrep", "watch"],
        preexec_fn=os.setsid,
        stdout=open(f"/tmp/mgrep-watch-command-{session_id}.log", "w"),
        stderr=open(f"/tmp/mgrep-watch-command-{session_id}.log", "w"),
    )

    debug_log(f"Started mgrep watch process: {process.pid} (session {session_id})")
    with open(pid_file, "w", encoding="utf-8") as handle:
        handle.write(str(process.pid))

    response = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "You must load mgrep skill for searching and exploring rather than grep",
        }
    }
    print(json.dumps(response))
    sys.exit(0)
