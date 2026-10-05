# Repository Context for the AI Coding Assistant
(Also copy to `.github/copilot-instructions.md` / `CLAUDE.md` depending on the tool.)

## Project
Student CGPA Performance Management System (Python 3.10+). Package: `src/student_performance`.

## Domain rules
- CGPA = sum(grade_point * credits) / sum(credits)  (credit-weighted, NOT a plain average).
- Grade scale is defined in `config/grade_scale.json` (10-point scale). Do not hard-code it.
- Failed course (F) has 0 grade points but its credits still count in the denominator.

## Coding standards
- Format with Black, lint with Ruff (rules in pyproject.toml). Line length 88.
- Type hints and docstrings on all public functions.
- Raise `ValueError` for invalid input; never silently ignore it.
- Tests with pytest in `tests/`, mirror module names, aim for >= 90% coverage.

## Rules for the AI
- Only modify files I name. Propose a diff; do not rewrite unrelated code.
- No new dependencies without asking.
- Never read or output `.env`, keys, or real student data.

## Out of scope / excluded from AI context
`.env`, `data/real/`, `*.pem`, `*.key` (also listed in .gitignore and the assistant ignore file).
