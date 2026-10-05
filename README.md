# Student CGPA Performance Management System

Small Python project used for the "AI-Augmented Software Development Environment" experiment.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

## Daily workflow
```bash
black . && ruff check . && pytest --cov=src
```
See `docs/AI_ENGINEERING_JOURNAL.md` for AI usage log and `CONTEXT.md` for the context given to the AI assistant.
