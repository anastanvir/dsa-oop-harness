# DocuMind — AI Document Processing Pipeline

**28-day production-grade Python grind.** Build a real AI document processing system
from scratch — no AI assistance on the code. You write every line.

> "You can architect systems at 30,000 feet. Now learn to build at sea level."

## The Project

DocuMind ingests documents, validates them, routes them through processing
pipelines, and serves them via FastAPI. Every DSA/OOP concept maps directly to
a production feature.

```
Week 1 │ OOP Foundation       → Document class, dunders, inheritance, factory
Week 2 │ Data Structures      → Lists, dicts, Big O optimization
Week 3 │ AI Agent Structures  → Queues, graphs, state machines
Week 4 │ FastAPI Capstone     → Full pipeline API
```

## Structure

```
documind/
├── src/documind/
│   ├── core/              # Week 1: Document class + processor hierarchy
│   ├── operations/        # Week 2: Collections, configs, optimization
│   ├── orchestration/     # Week 3: Queues, routing, state machines
│   └── api/               # Week 4: FastAPI endpoints
├── quizzes/
│   └── week1/             # Daily conceptual checks + weekly assessment
├── tests/                 # Validate your code — all must pass
├── CURRICULUM.md          # Full 28-day plan
├── NOTES.md               # Log blockers and insights
└── pyproject.toml
```

## Daily Workflow

```
 1. Quiz  →  quizzes/week1/dayN_quiz.py      (concept check)
 2. Code  →  src/documind/.../               (fill TODO stubs)
 3. Test  →  pytest tests/test_dayN.py -v     (all green = done)
 4. Commit →  git commit -m "Day N: <topic>"
 5. Log   →  confidence + SHA in the tracker
```

## The Core Rules

- **Zero AI on code.** You write every line. No Copilot, no ChatGPT, no Claude.
- **Tests must pass** before the day counts.
- **Commit every single day.** No exceptions.
- **Confidence ≤3?** Schedule a review on the week's final day.
- **Stuck >30 min?** Log the blocker in `NOTES.md` and move on.
- **No `any` types. No magic values. Guard clauses, not nested ifs.**

## Quick Start

```bash
pip install -e ".[dev]"
pytest tests/test_day1.py -v   # Will fail — you fill in the code
```

## Repo

[github.com/anastanvir/dsa-oop-harness](https://github.com/anastanvir/dsa-oop-harness)
