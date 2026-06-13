# DocuMind — AI Document Processing Pipeline

A production-grade system built from scratch over 28 days.
Each day adds real code. No throwaway exercises. Every concept maps to a feature you ship.

## Why This Project

You process documents through AI pipelines every day. This project mirrors exactly that:
ingest → validate → transform → route → store → serve. Every DSA/OOP concept maps to
a production concern you'll face building real AI backends.

## Weekly Roadmap

```
Week 1  │  OOP Foundation
────────┼────────────────────────────────────────────────────
Day 1   │  Document class — blueprint, self, constructor
Day 2   │  Class attributes, factory methods, multiple instances
Day 3   │  __repr__, __str__, __len__ — make objects readable
Day 4   │  __call__ for pipelines, __enter__/__exit__ for context
Day 5   │  Inheritance — BaseDocument → TextDocument, JSONDocument
Day 6   │  super(), method overriding, abstract base classes
Day 7   │  Full class hierarchy + factory — ship Week 1
────────┼────────────────────────────────────────────────────
Week 2  │  Data Structures & Flow
Day 1   │  Batch processing with lists — DocumentCollection
Day 2   │  Filtering, mapping, sorting collections
Day 3   │  Copy vs reference — avoid pipeline bugs
Day 4   │  Config management with dicts — PipelineConfig
Day 5   │  Deeply nested JSON parsing — API response handling
Day 6   │  Big O profiling — find bottlenecks in your pipeline
Day 7   │  Rewrite O(n²) → O(n) — ship Week 2
────────┼────────────────────────────────────────────────────
Week 3  │  Complex Structures for AI Agents
Day 1   │  Processing Queue (FIFO) — manage document backlogs
Day 2   │  Priority Queue — urgent documents first
Day 3   │  Tree traversal — document category hierarchy
Day 4   │  Directed Graph — multi-stage pipeline routing
Day 5   │  Decision Graph — conditional document routing
Day 6   │  State Machine — pipeline stage transitions
Day 7   │  Full Orchestrator — ship Week 3
────────┼────────────────────────────────────────────────────
Week 4  │  FastAPI Capstone — Deterministic AI Pipeline
Day 1   │  Scaffold FastAPI app + dependency injection
Day 2   │  POST /ingest — receive documents via API
Day 3   │  Validate + clean with Big O awareness
Day 4   │  Store results in config dicts
Day 5   │  Pass clean data to model/API harness
Day 6   │  Error handling, structured logging, type hints
Day 7   │  Tests, README, demo — public proof of work
```

## Your Daily Routine

```
09:00  │  Cron reminder + day's topic hits your chat
09:05  │  Open CURRICULUM.md → read today's section
09:10  │  Open the day's quiz → confirm you understand concepts
09:15  │  Write the code in the project files (TODO markers)
09:45  │  Run tests → all green?
09:50  │  git commit with SHA
09:55  │  Update the Excel tracker (confidence, commit link)
       │  Stuck? Log in NOTES.md, move on
```

## Rule of the Beast

- **No AI to write the code.** You write every line.
- **No AI to debug.** Read the traceback, read the docs, reason it out.
- **If truly stuck (30+ min):** Log the exact blocker. Ask *me* one specific question.
- **Tests must pass** before the day counts.
- **Commit every day.** Miss a day and the chain breaks.
- **Confidence ≤3?** Schedule a review — revisit the topic on Day 7 of the week.

## The Project Skeleton

```
documind/
├── src/documind/          # ← YOU build this, day by day
│   ├── __init__.py
│   ├── core/              # Week 1
│   │   ├── document.py
│   │   ├── collection.py
│   │   ├── pipeline.py
│   │   └── processors.py
│   ├── operations/        # Week 2
│   ├── orchestration/     # Week 3
│   └── api/               # Week 4
├── quizzes/               # Daily conceptual checks
│   └── week1/
├── tests/                 # Validates your code
│   └── test_*.py
├── CURRICULUM.md          # This file
├── NOTES.md               # Your blockers + insights
└── pyproject.toml
```
