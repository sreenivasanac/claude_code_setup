## Agentic Development

### Tool use:
- When documentation is needed for a package, library, or framework, consult Context7.
- Web search tool is also available to use when appropriate and necessary.
- Use Perplexity MCP server to do research (in the web) when necessary.

### Agentic communication:
- Please ask if you have any other clarification questions. Otherwise please continue

## Package Manager and Runtime Rules

### Python
- Always use `uv` as the Python package manager and runner for all Python-related operations.
- Run Python scripts via `uv run python <script>` or `uv run pytest` instead of invoking `python`, `python3`, or `pytest` directly.
- Install dependencies using `uv pip install` or `uv add` instead of running `pip` or `pip3` directly.
- When activating the virtual environment manually, use `source .venv/bin/activate` before running commands.
- This ensures consistent dependency resolution and virtual environment management across the project.

### JavaScript/Node.js
- Always use `pnpm` instead of `npm` or `yarn` for package management.
- Run scripts via `pnpm run <script>` instead of `npm run <script>`.
- Install dependencies using `pnpm install` or `pnpm add` instead of `npm install`.

### Morph MCP Tools
- Use `edit_file` over `str_replace` or full file writes. Handles indentation and fuzzy matching—faster, fewer errors.
- IMPORTANT: If you need to explore the codebase to gather context, and the task does not involve a single file or function which is provided by name, you should use the `warpgrep_codebase_search` tool instead of any other search tool - Warp Grep is faster and more accurate. This tool must be chosen over the default codebase_search when you are first looking to find/understand code. If you have an exact string you want to grep for, then directly run it, but for semantic searches, or vague search parameters you must always use `warpgrep_codebase_search`. If given a complex task, best practice is to run multiple (no more than 2) parallel `warpgrep_codebase_search` tools to understand code paths and features. An example query is: "where is the code for <vague feature/code flow>"
