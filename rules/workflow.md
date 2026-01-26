# Workflow & Implementation Rules

## Clarify requirements
**Applies to**: Any task with unclear requirements
**Rule**: Stop and ask before implementing.

## Default to action
**Applies to**: Tasks with clear requirements
**Rule**: Proceed without waiting for additional prompts.

## Significant deviations
**Applies to**: Stack/pattern choices
**Rule**: Default to modern, stable, well-supported stacks and patterns; get explicit approval before significant deviations.

## Implementation principles
**Applies to**: All code changes
**Rule**: Keep code simple and straightforward; avoid unnecessary edge cases far from expected behavior.

**Applies to**: Non-obvious functions/blocks
**Rule**: Add a short docstring or inline comment explaining intent.

**Applies to**: Requirement TODOs
**Rule**: Capture them as `TODO:` comments in relevant code.

**Applies to**: Configuration/branding
**Rule**: Centralize configuration and branding in constants that are easy to update.

## Documentation updates
**Applies to**: When changes would make docs misleading
**Rule**: Ask before updating `README.md` or other docs (do not update docs unless explicitly requested).
