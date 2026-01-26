---
description: Commit staged files with a clear, conventional message
allowed-tools:
  - git status
  - git diff --cached
  - git diff --cached --stat
  - git diff --cached --patch --no-color -- <file>
  - git log --oneline -5
  - git commit -m <message>
---

This command assumes **you already staged** the changes you want to commit.

## Review staged changes (minimal + deterministic)

1) Check the current branch + staged/unstaged status:

- `git status -sb`

2) **Fail fast** if nothing is staged:

- `git diff --cached --quiet`
  - If exit code is `0`, stop: "No staged changes. Stage files first (git add …)."
  - If exit code is `1`, there are staged changes (continue).

3) Show a compact summary of what will be committed:

- `git diff --cached --stat`

4) Show a staged patch preview **per file** (first 400 lines each):

- `git diff --cached --patch --no-color -- README.md | sed -n '1,400p'`
- `git diff --cached --patch --no-color -- <path/to/file> | sed -n '1,400p'`
  - Run the above once for each staged file path.

5) Pull recent commit style for context:

- `git log --oneline -5`

## Craft the commit message (Conventional Commits; scope required)

Use:

```
<type>(<scope>): <description>

<body: 2–5 lines summarizing the changes>

Co-authored-by: factory-droid[bot] <138933559+factory-droid[bot]@users.noreply.github.com>
```

- Scope is **required** (examples: `readme`, `prompts`, `solution-a`, `solution-b`, `solution-c`, `docs`).
- Main line should describe the dominant theme, not enumerate files.
- Body should summarize key impacts in 2–5 lines.

Type prefixes:
- `feat`, `fix`, `docs`, `chore`, `refactor`, `ci`, `test`, `build`, `perf`, `style`
- Use `!` or a `BREAKING CHANGE:` footer when applicable.

## Example commit

```bash
git commit -m "feat(visualization): assume bundled umap and streamlit deps

Promote umap-learn, numba, and streamlit to core requirements and drop PCA/Streamlit fallbacks.
Add reusable HTML template helper plus Streamlit stubs to keep tests passing.

Co-authored-by: factory-droid[bot] <138933559+factory-droid[bot]@users.noreply.github.com>"
```

Note: Multiline commit messages must be enclosed within double quotes.

## Conventional Commits guidelines

- Aims for explicit, SemVer-compatible history to enable automation.
- Commits are case-insensitive except for uppercase `BREAKING CHANGE`.
- Avoid enumerating all changes in the description; use the body for details.
- Type is mandatory; description follows colon/space.

## High-level PR overview and message guidance

When preparing commits, review the changes at a high level to understand what the commit is trying to accomplish overall.
Use context from recent commit messages (`git log --oneline -5`) to match the repository's style.
Craft a cohesive summary focusing on primary goals and impacts, not a file-by-file enumeration.

## Commit (run automatically)

Run:

```bash
git commit -m "<subject>\n\n<body>\n\nCo-authored-by: factory-droid[bot] <138933559+factory-droid[bot]@users.noreply.github.com>"
```

## Guardrails (avoid command explosion)

- Do **not** run `git add` or otherwise modify staging.
- Do **not** run multiple overlapping staged diff commands; use `--stat` once and bounded per-file patch previews.
- If a staged patch is too large to review in preview, keep `--stat` and ask the user to review locally with `git diff --cached -- <file>`.