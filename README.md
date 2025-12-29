# Claude Code / Factory CLI Setup

Personal configuration for Claude Code and Factory CLI, including custom commands, skills, and coding guidelines.

## Directory Structure

```
.
├── AGENTS.md          # Coding guidelines and rules for AI agents
├── commands/          # Custom slash commands
│   ├── commit-files.md    # /commit-files - Conventional commit helper
│   └── improve-prompt.md  # /improve-prompt - Prompt optimization
├── hooks/             # Git/CLI hooks (placeholder)
├── skills/            # Custom skills
│   └── mgrep/         # Semantic grep skill
└── README.md
```

## AGENTS.md - Coding Guidelines

Defines rules and conventions for AI coding agents:

- **Tool Usage**: Context7 for docs, Perplexity MCP for web research, WarpGrep for codebase search
- **Python**: Use `uv` for all package management (`uv run`, `uv pip install`, `uv add`)
- **JavaScript/Node.js**: Use `pnpm` instead of npm/yarn
- **Morph MCP**: Prefer `edit_file` over `str_replace` for file edits

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
Semantic grep for local files - superior to built-in search tools.

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
