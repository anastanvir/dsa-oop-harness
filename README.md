# DSA + OOP Harness

**4-week production-grade Python grind** — build the fundamentals you skipped so AI becomes a tool, not a crutch.

> You can architect systems at 30,000 feet. Now learn to build at sea level.

## The Pact

1. **No AI to write exercises.** Read the lesson, write the code, run the tests. The entire point is to develop the muscle memory yourself.
2. **Commit every single day.** The tracker holds you accountable.
3. **Rate honestly.** 1–5 confidence. ≤3 means revisit.
4. **Time-box.** If a day's topic isn't clicking, log the blocker and move on.

## Structure

```
src/
├── week1_oop/           # Classes, self, dunders, inheritance, mini-build
├── week2_linear/        # Lists, dicts, Big O
├── week3_complex/       # Stacks, queues, trees, graphs, state machines
└── capstone/            # FastAPI deterministic AI data pipeline
tests/                   # Tests mirror src/ — they validate your work
```

## Quick Start

```bash
# Install dependencies
pip install -e ".[dev]"

# Run a day's tests
pytest tests/week1/test_day1.py -v

# Run all tests
pytest -v
```

## Daily Workflow

1. Open the day's lesson: `src/week1_oop/day1_classes_self/lesson.py`
2. Read the concept + examples
3. Complete the `TODO` / `# YOUR CODE HERE` sections
4. Run the tests: `pytest tests/week1/test_day1.py -v`
5. **All green?** Commit with the day's SHA
6. **Stuck?** Log the blocker in `NOTES.md` and move to the next day
7. Update the Excel tracker with your confidence + commit link

## Rules

- **No `any` types.** Strict typing everywhere.
- **No magic values.** Constants and enums.
- **Guard clauses, not nested ifs.**
- **Tests must pass** before the day counts as done.
