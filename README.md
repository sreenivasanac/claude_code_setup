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

## AI Coding Setup — MCP Servers

MCP servers that are useful to install when setting up an AI-augmented coding environment / CLI (e.g., Claude Code / Codex / Factory).

### MCP servers recommended to install

- **morph-mcp** — local code editing + semantic repo discovery (`edit_file`, `warpgrep_codebase_search`)
  - More details (mgrep/warpgrep): https://github.com/mixedbread-ai/mgrep
  - Run: `npx -y @morphllm/morphmcp`
  - Needs: `MORPH_API_KEY`

- **context7** — updated library/framework documentation retrieval
  - Avoids relying on outdated, generic library APIs.
  - MCP Repo: https://github.com/upstash/context7
  - Endpoint: `https://mcp.context7.com/mcp`
  - Needs: Context7 API key/token (set via headers in your MCP config)

- **nano-banana-pro** — diagram/image generation (Gemini AI - Nano Banana Pro Image model)
  - Details: https://github.com/mrafaeldie12/nano-banana-pro-mcp
  - Run: `npx -y @rafarafarafa/nano-banana-pro-mcp`
  - Needs: `GEMINI_API_KEY`

- **perplexity** — web research / reasoning
  - Run: `npx -y perplexity-mcp`
  - Needs: `PERPLEXITY_API_KEY`

- **brave-search** — web search
  - Run: `npx -y @brave/brave-search-mcp-server`
  - Needs: `BRAVE_API_KEY`

- **chrome-devtools** — browser-based testing / debugging
  - Run: `npx -y chrome-devtools-mcp@latest`

- **grep-mcp** — public GitHub/code search
  - Run: `uvx grep-mcp`

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

### Other useful skills

- **prompt-refiner** — rewrites rough task descriptions into clearer, more actionable prompts.
- **prompt-refiner-gpt** — prompt refinement patterns tuned for GPT/Codex.
- **react-useeffect** — `useEffect` best practices from React docs (and when not to use Effects).
- **skill-creator** — guidance for creating/updating skills (structure, metadata, resources).
- **web-design-guidelines** — UI/UX + accessibility review against Web Interface Guidelines.

#### Optional skills to add

- **planning-with-files** — Manus-style persistent markdown files for planning, progress tracking, and knowledge storage.
  https://github.com/jarrodwatts/claude-code-config/tree/main/skills/planning-with-files
