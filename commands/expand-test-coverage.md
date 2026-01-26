---
name: Expand Unit Tests
description: Increase test coverage by targeting untested branches and edge cases
tags: testing, coverage, unit-tests
---
# Expand Unit Tests
Expand existing unit tests adapted to project's testing framework:
1. **Analyze coverage**: Run coverage report and scan all major files/modules in the codebase to identify important features/cases with little or no test coverage
2. **Identify gaps**: Review existing tests alongside the implementation to spot missing scenarios (logical branches, error paths, boundary conditions, null/empty inputs) where new tests should be added
3. **Write tests** using project's framework:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **Target specific scenarios**:
   - Error handling and exceptions
   - Boundary values (min/max, empty, null)
   - Edge cases and corner cases
   - State transitions and side effects
5. **Verify improvement**: Run coverage again, confirm measurable increase
Present new test code blocks only. Follow existing test patterns and naming conventions.
