# Repo Boundaries & Hygiene Rules

**Applies to**: Prompt archives
**Rule**: Avoid reading or modifying files inside `used_prompts/` folder unless explicitly asked.

## Large refactors
**Applies to**: Moving a folder with many files - which is already being checked into and tracked by git, to another location
**Rule**: Prefer `git mv` over `mv` so Git tracks the move as renames instead of entire files delete and entire file create.
