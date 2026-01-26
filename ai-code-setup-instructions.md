# AI Coding Setup — MCP Servers

This page lists MCP servers that are useful to install when setting up an AI-augmented coding environment / CLI (e.g., Claude Code / Codex / Factory).

## MCP servers recommended to install

- **morph-mcp** — local code editing + semantic repo discovery (`edit_file`, `warpgrep_codebase_search`)
  - Morph-MCP with mgrep github repo with more details and instructions: https://github.com/mixedbread-ai/mgrep
  - Run: `npx -y @morphllm/morphmcp`
  - Needs: `MORPH_API_KEY`

- **context7** — updated library/framework documentation retrieval
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
  - Useful when we want latest updated ways to do something. This search comes with citations.
  - Run: `npx -y perplexity-mcp`
  - Needs: `PERPLEXITY_API_KEY`

- **brave-search** — web search
  - Run: `npx -y @brave/brave-search-mcp-server`
  - Needs: `BRAVE_API_KEY`

- **chrome-devtools** — browser-based testing / debugging
  - We can directly give AI-augmented-CLI access to browser, for it to open the URL, check the browser output, check if any browser errors logged, etc.
  - Run: `npx -y chrome-devtools-mcp@latest`

- **grep-mcp** — public GitHub/code search
  - Run: `uvx grep-mcp`
