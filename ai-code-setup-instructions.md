# AI Coding Setup — MCP Servers

This page lists MCP servers that are useful to install when setting up an AI-augmented coding environment / CLI (e.g., Claude Code / Codex / Factory).

## MCP servers recommended to install

- **morph-mcp** — local code editing + semantic repo discovery (`edit_file`, `warpgrep_codebase_search`)
  - Morph-MCP with mgrep github repo with more details and instructions: https://github.com/mixedbread-ai/mgrep
  - Run: `npx -y @morphllm/morphmcp`
  - Needs: `MORPH_API_KEY`

- **context7** — updated library/framework documentation retrieval
  - avoids LLMs rely on outdated generic library APIs based on year-old training data.
  - MCP Repo: https://github.com/upstash/context7
  - Endpoint: `https://mcp.context7.com/mcp`
  - Needs: Context7 API key/token (set via headers in your MCP config)

- **nano-banana-pro** — diagram/image generation (Gemini AI - Nano Banana Pro Image model)
  - Excellent image 
  - This can be run as a skill as well.
  - Details https://github.com/mrafaeldie12/nano-banana-pro-mcp
  - Run: `npx -y @rafarafarafa/nano-banana-pro-mcp`
  - Needs: `GEMINI_API_KEY`

- **perplexity** — web research / reasoning
  - Useful when we want latest updated ways to do something. Perplexity searches top 20 results and gives answer.
  - Run: `npx -y perplexity-mcp`
  - Needs: `PERPLEXITY_API_KEY`

- **brave-search** — web search
  - Similar to Google search to fetch something quick.
  - Run: `npx -y @brave/brave-search-mcp-server`
  - Needs: `BRAVE_API_KEY`

- **chrome-devtools** — browser-based testing / debugging
  - We can directly give AI-augmented-CLI access to browser, for it to open the URL, check the browser output, check if any browser errors logged, etc.
  - Run: `npx -y chrome-devtools-mcp@latest`

- **grep-mcp** — public GitHub/code search
  - Very efficient Github / code search - to find suitable github repositories, or their documentation.
  - Run: `uvx grep-mcp`

## Skills

- **mgrep** — semantic local file search for fast repo exploration.
  - Prefer this over grep/rg; ask in natural language (e.g., `mgrep "Where is auth handled?"`).

- **prompt-refiner** — rewrites rough task descriptions into clearer, more actionable prompts.
  - Use when you want tighter constraints / acceptance criteria before handing a task to a model.

- **prompt-refiner-gpt** — prompt refinement patterns tuned for GPT/Codex.
  - Adds explicit role, step-by-step procedure, and structured output requirements.

- **react-useeffect** — `useEffect` best practices from React docs (and when not to use Effects).
  - Useful for reviewing hooks code and replacing effect-driven derived state with better patterns.

- **skill-creator** — guidance for creating/updating skills (structure, metadata, resources).
  - Use when you’re adding a new skill or iterating on an existing one.

- **web-design-guidelines** — UI/UX + accessibility review against Web Interface Guidelines.
  - Use when you want an audit of UI code for best-practice compliance.

### Optional skills to add

- **planning-with-files** — Manus-style persistent markdown files for planning, progress tracking, and knowledge storage. Use for complex tasks, multi-step projects, research tasks, or anytime you want structured progress tracking.
  https://github.com/jarrodwatts/claude-code-config/tree/main/skills/planning-with-files

