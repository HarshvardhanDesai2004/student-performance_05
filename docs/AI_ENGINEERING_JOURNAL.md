# AI Engineering Journal

**Tool:** <AI assistant used, e.g. GitHub Copilot / Claude / Gemini Code Assist>  **IDE:** VS Code
**Context given:** `CONTEXT.md` (+ `.github/copilot-instructions.md`). Excluded: `.env`, `data/real/`, keys.
**Rule:** AI output is a *suggestion*. Nothing is merged until a human has read, run and tested it.

| # | Task type | Prompt (summary) | AI output | Human validation / decision | Commit |
|---|-----------|------------------|-----------|-----------------------------|--------|
| 1 | Code generation | "Write `calculate_cgpa(courses)` for (grade, credits) pairs using the grade scale in CONTEXT.md" | 10-line function, hard-coded grade dict | Read it: **accepted as draft only**; spotted it ignored credits and validation, left for tests to confirm | feat: AI-generated CGPA calculator draft |
| 2 | Code explanation | "Explain `calculate_cgpa` line by line and state its assumptions" | Explained loop and `round`; noted it divides by number of courses | Compared with the CGPA formula in CONTEXT.md -> mismatch noticed: **hypothesis: wrong denominator** | (no code change) |
| 3 | Test generation | "Write pytest tests: single course, weighted average, F-grade credits, empty input, invalid grade, non-positive credits" | 6 tests | Recomputed expected values by hand ((10*4+6*2)/6 = 8.67; (9*3+0)/6 = 4.5). Tests are correct; **accepted** | test: add AI-generated pytest suite |
| 4 | Debugging | Pasted failing pytest output (6 failed: 32.0 != 8.0, ZeroDivisionError, KeyError) | Suggested dividing by total credits and adding validation | Reproduced failure first, applied fix, re-ran: 6 passed. **Accepted after verification** | fix: weight CGPA by credits... |
| 5 | Refactoring | "Refactor to read the scale from config/grade_scale.json, add type hints/docstrings, keep behaviour" | New loader, `_validate`, typed signature, docstring | Ran Black, Ruff, pytest (14 passed, 100% coverage). Rejected an extra suggestion to add `pydantic` (**violates "no new dependencies"**) | refactor: load grade scale from config... |
| 6 | Feature + review | "Add `performance_band(cgpa)`" | Band function with thresholds | Thresholds are a *policy* decision: confirmed with the course rule (>=8.5 Distinction ...), added boundary tests | same commit |

## Reflection
- **AI-suggested vs human-decided:** AI proposed code, tests and a fix; the human decided correctness (formula, thresholds), dependencies and what was merged.
- **Bug caught:** AI draft computed a plain mean of grade points. Only the tests and a review against the domain rule exposed it -> tests are the safety net for AI code.
- **Security/privacy:** no secrets, real student records or personal data were pasted into prompts; `.env` is git-ignored and listed in `.aiignore`.
- **Limitations seen:** AI over-engineers (extra dependency), and is confident even when wrong.
