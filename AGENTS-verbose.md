(Note: This is a verbose version of AGENTS.md file, different from FactoryAI recommendation to give Agent rules in their onw rules format. If you prefer this verbose version, you can renaming this file to AGENTS.md and use this)
# Agent Instructions

## 1) Agentic development

### 1.1 Tool use
- Prefer Context7 for package/library/framework documentation.
- Use web search and/or the Perplexity MCP server when Context7 is insufficient or freshness matters.
- For system design / system architecture diagrams, use the Nano Banana Pro MCP server.
- For searching GitHub (code and documentation across public repos), consider using the `grep-mcp` MCP server.
- For browser-based testing and inspecting frontend error messages, consider using the `chrome-devtools` MCP server.
- For general web search, consider using the `brave-search` MCP tool/server.

### 1.2 Communication
- If an important requirement is unclear, stop and ask before implementing.
- Otherwise, proceed without waiting for additional prompts.

### 1.2.1 Significant deviations
- Default to modern, stable, and well-supported stacks and patterns.
- Secure explicit approval before making any significant deviation from these rules.

### 1.3 Implementation principles
- Keep code simple and straightforward; avoid unnecessary edge cases far from the expected behavior.
- For non-obvious functions/blocks, add a short docstring or inline comment explaining intent.
- If there are TODOs from the requirements, capture them as `TODO:` comments in the relevant code.
- Take time to think through changes; don’t rush.
- Centralize configuration and branding in constants that are easy to update.
- After major code changes, update `README.md` if it would otherwise become outdated or misleading.

### 1.4 Optional development notes
- When useful (not mandatory), log non-intuitive assumptions/decisions/future work/questions to `agentic_development_docs/agent_communication_docs/`:
  - `assumptions_made_by_agent.md`
  - `design_decision.md`
  - `future_work.md`
  - `questions.md`
- Create/update development notes only when they help ongoing work (don’t write docs “just because”).
- Feel free to create new markdown files when useful for logging progress or aiding future implementation.

### 1.5 Post-implementation updates
- After making implementation changes, update relevant project design plan files accordingly.
- If you discover useful rules during implementation, feel free to append them to `~/.factory/AGENTS.md` file

## 2) Package manager and runtime rules

### 2.1 Python
- Always use `uv` as the Python package manager and runner for all Python-related operations.
- Run scripts/tests via `uv run python <script>` / `uv run pytest` (avoid calling `python`/`python3`/`pytest` directly).
- Install dependencies using `uv pip install` or `uv add` (avoid `pip`/`pip3`).
- If manually activating a virtual environment, use `source .venv/bin/activate`.

### 2.2 JavaScript/Node.js
- Always use `pnpm` instead of `npm` or `yarn`.
- Run scripts via `pnpm run <script>`.
- Install dependencies via `pnpm install` / `pnpm add`.

## 3) Morph MCP tools
- Prefer `edit_file` over search/replace or full-file rewrites; it’s faster and less error-prone.
- Fast apply: prefer `edit_file` over `str_replace` or full-file writes; it works with partial snippets (no need to paste full file content).
- For initial codebase exploration (when you don’t already know the exact file/function), use `warpgrep_codebase_search`.
- WarpGrep: use it early for broader semantic queries (e.g., “Find the XYZ flow”, “How does XYZ work?”, “Where is XYZ handled?”, “Where is <error message> coming from?”), not for pinpoint keyword searches.

## 3.1 mgrep (semantic search)
- Use `mgrep` for intent/feature discovery and onboarding; use `grep`/`ripgrep` for exact string/symbol/regex matches.
- If available, keep an index running in large repos: `mgrep watch`.
- Common usage:
  - `mgrep "<question>" [path]`
  - `mgrep -m <N> "<question>"`
  - `mgrep -c "<question>"` (show result content)
  - `mgrep -a/--answer "<question>"` (answer based on matches)
- Web search (when needed): `mgrep --web --answer "<question>"`.
- Auth:
  - Prefer interactive login: `mgrep login`.
  - For headless/CI: set `MXBAI_API_KEY`.

## 4) Repo boundaries
- Do not modify the `old_code/` folder. Use it only for inspiration; do not copy code verbatim.
- Avoid reading or modifying `agentic_development_docs/used_prompts/` unless explicitly asked.
- When moving/renaming many files during refactors, prefer `git mv` over `mv` so Git records the changes as renames/moves instead of delete+add.

## 5) Documentation references (when relevant)
- LiteLLM embeddings: https://docs.litellm.ai/docs/embedding/supported_embedding
- LiteLLM docs indices: https://docs.litellm.ai/llms.txt and https://docs.litellm.ai/llms-full.txt
- Ollama docs indices: https://docs.ollama.com/llms.txt and https://docs.ollama.com/llms-full.txt
- Tauri docs: https://tauri.app/llms.txt and https://tauri.app/llms-full.txt (start: https://tauri.app/start/)
- Agno docs indices: https://docs.agno.com/llms.txt and https://docs.agno.com/llms-full.txt
