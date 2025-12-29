---
description: Commit staged files with a clear, conventional message
---

All required files that need to be git committed are already staged. Craft a concise commit message that follows best practices.

## Review the staged diff

Use the commands:

- `git status -sb`
- `git diff --cached`

## Craft the commit message

Follow the Conventional Commits format:

```
<type>[scope]: <description>

[body: 2–5 lines summarizing the changes]
```

In the main line of the commit message, describe the dominant theme or primary change rather than enumerating every file change. In the next line(s), give a 2–5 line summary of the changes.

### Type prefixes

- feat: for new features
- fix: for bug fixes
- chore:, docs:, style:, refactor:, perf:, test:, build:, ci:, etc., for other changes
- Add ! or a BREAKING CHANGE: footer for breaking updates

## Commit using a bash tool call

Invoke the bash tool to run the commit command:

```
git commit -m "<generated commit message along with the description"
```
Remember that the generated commit message is going to be multiline commit message - all of it has to be enclosed within double quotes. See Example commit.

## Example commit

git commit -m "feat(visualization): assume bundled
umap and streamlit deps.

Promote umap-learn, numba, and streamlit to core
requirements and drop PCA/Streamlit fallbacks.
Add reusable HTML template helper plus Streamlit
stubs to keep tests passing."

## Conventional Commits Guidelines

- Aims for explicit, SemVer-compatible history to enable automation.
- Commits are case-insensitive except for uppercase BREAKING CHANGE.
- Avoid: Enumerating all changes in the description; use body for details.
- Key Rules: Type is mandatory; description follows colon/space;

## High-Level PR Overview and Message Guidance

When preparing commits or pull requests, the AI should review the changes at a high level to understand what the PR is trying to accomplish overall.
The AI can use context from the commit messages of the last 5 commits using the git command `git log --oneline -5`.
The Git Pull Request message need not necessarily be a concatenation of what changed in each file; instead, craft a cohesive summary focusing on the primary goals and impacts.