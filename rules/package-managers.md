# Package Manager & Runtime Rules

## Python
**Applies to**: All Python-related operations
**Rule**: Always use `uv` as the Python package manager and runner.

- Run scripts/tests via `uv run python <script>` / `uv run pytest` (avoid calling `python`/`python3`/`pytest` directly)
- Install dependencies using `uv pip install` or `uv add` (avoid `pip`/`pip3`)
- If manually activating a virtual environment: `source .venv/bin/activate`

## JavaScript / Node.js
**Applies to**: All Node.js operations
**Rule**: Always use `pnpm` instead of `npm` or `yarn`.

- Run scripts via `pnpm run <script>`
- Install dependencies via `pnpm install` / `pnpm add`
