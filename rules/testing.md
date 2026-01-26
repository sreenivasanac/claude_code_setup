# Testing Rules

## Why this matters
Slow or flaky tests are the #1 cause of wasted tokens. Each retry costs a full response cycle.

| Test Characteristic | Impact on Tokens |
| --- | --- |
| Fast tests (< 30s) | Droid verifies changes immediately |
| Slow tests (> 2min) | Droid may skip verification or waste context waiting |
| Flaky tests | False failures cause debugging cycles |
| No tests | Droid can’t verify changes, more back-and-forth |

## Testing
- Run single file: `npm test -- path/to/file.test.ts`
- Run fast smoke tests: `npm test -- --testPathPattern=smoke`
- Full suite takes ~3 minutes, use `--bail` for early exit on failure
