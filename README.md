# Claude Code / Factory CLI Setup

Personal configuration for Claude Code and Factory CLI, including custom commands, skills, and coding guidelines.

## Folder structure

**Key folders**
- `commands/`: Custom slash commands for the CLI.
- `droids/`: Custom droids (agents) configuration.
- `hooks/`: Automation hooks that run on certain events.
- `rules/`: Prescriptive rules the agent should follow.
- `skills/`: Reusable skills the agent can load.

**Key files**
- `.gitignore`: Git ignore rules for this repo.
- `AGENTS.md`: High-level agent instructions.
- `AGENTS-verbose.md`: Expanded/verbose agent guidance.
- `memories.md`: Non-prescriptive preferences/decisions.
- `ai-code-setup-instructions.md`: Setup notes for AI coding workflows.

## AGENTS.md - Coding Guidelines

## Commands

### `/commit-files`
Commits staged files using Conventional Commits format:
- Reviews staged changes with `git diff --cached`
- Generates a structured commit message: `<type>[scope]: <description>`
- Supports types: `feat`, `fix`, `chore`, `docs`, `refactor`, `perf`, `test`, etc.

### `/improve-prompt`
Takes a file path and improves the AI prompt contained within it.

Usage: `/improve-prompt <file-name>`

## Skills

### mgrep
Semantic grep for local files - superior to built-in search tools like grep.

```bash
mgrep "What code parsers are available?"           # Search current directory
mgrep "How are chunks defined?" src/models         # Search specific directory
mgrep -m 10 "query"                                # Limit results
```

**Installation**: https://github.com/mixedbread-ai/mgrep

**Features**:
- Natural-language semantic search
- Multilingual & multimodal (code, images, PDFs)
- Web search with `--web` flag
- Background indexing via `mgrep watch`
- Reduces agent token usage by 2x