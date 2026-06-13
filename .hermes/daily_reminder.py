#!/usr/bin/env python3
"""DocuMind — Daily reminder script.

Calculates the current day in the 28-day curriculum (starting July 6, 2026)
and outputs the day's reminder message with project context.
"""

from __future__ import annotations
from datetime import date
import os
import sys

START_DATE = date(2026, 7, 6)  # Monday

CURRICULUM: list[dict] = [
    # ═══════════════════════════════════════════════════════════════
    # Week 1 — OOP Foundation
    # ═══════════════════════════════════════════════════════════════
    {"week": 1, "day": 1, "topic": "Document Class",
     "focus": "Blueprint, self, constructor — build the core Document class",
     "why": "Every PyTorch/sklearn model is an instance of a class. Document is your first.",
     "path": "src/documind/core/document.py",
     "test": "tests/test_day1.py",
     "quiz": "quizzes/week1/day1_quiz.py",
     "project_file": "src/documind/core/document.py"},
    {"week": 1, "day": 2, "topic": "Class Attributes & Factory",
     "focus": "Class-level state, classmethods, @property",
     "why": "Shared config across all instances; factory pattern for creating documents",
     "path": "src/documind/core/document.py",
     "test": "tests/test_day2.py",
     "quiz": "quizzes/week1/day2_quiz.py",
     "project_file": "src/documind/core/document.py"},
    {"week": 1, "day": 3, "topic": "Dunder Methods I",
     "focus": "__repr__, __str__, __len__, __eq__ — make objects readable",
     "why": "PyTorch modules use __repr__; len() works on any collection",
     "path": "src/documind/core/document.py",
     "test": "tests/test_day3.py",
     "quiz": "quizzes/week1/day3_quiz.py",
     "project_file": "src/documind/core/document.py"},
    {"week": 1, "day": 4, "topic": "Dunder Methods II",
     "focus": "__call__, __enter__/__exit__, __add__ — callable & composable objects",
     "why": "model(x) is __call__; with open() is __enter__/__exit__",
     "path": "src/documind/core/document.py",
     "test": "tests/test_day4.py",
     "quiz": "quizzes/week1/day4_quiz.py",
     "project_file": "src/documind/core/document.py"},
    {"week": 1, "day": 5, "topic": "Inheritance & Base Classes",
     "focus": "BaseDocument → TextDocument, JSONDocument, CSVDocument",
     "why": "nn.Module is a base class — you inherit, override forward()",
     "path": "src/documind/core/processors.py",
     "test": "tests/test_day5.py",
     "quiz": "quizzes/week1/day5_quiz.py",
     "project_file": "src/documind/core/processors.py"},
    {"week": 1, "day": 6, "topic": "Abstract Classes & Overriding",
     "focus": "ABC, abstractmethod, super(), validate() contracts",
     "why": "Framework designers define interfaces; you implement the logic",
     "path": "src/documind/core/processors.py",
     "test": "tests/test_day6.py",
     "quiz": "quizzes/week1/day6_quiz.py",
     "project_file": "src/documind/core/processors.py"},
    {"week": 1, "day": 7, "topic": "Factory Pattern & Polymorphism",
     "focus": "DocumentFactory, chain_process, polymorphic dispatch",
     "why": "Write code that works on ANY document type without if/elif chains",
     "path": "src/documind/core/processors.py",
     "test": "tests/test_day7.py",
     "quiz": "quizzes/week1/day7_quiz.py",
     "project_file": "src/documind/core/processors.py"},
    # ═══════════════════════════════════════════════════════════════
    # Week 2 — Data Structures & Flow
    # ═══════════════════════════════════════════════════════════════
    {"week": 2, "day": 1, "topic": "Batch Processing w/ Lists",
     "focus": "DocumentCollection — indexing, slicing, appending batches",
     "why": "Model inputs x and outputs y live in arrays",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 2, "topic": "Filter, Map, Sort",
     "focus": "Transforming collections with comprehensions and built-ins",
     "why": "Clean data pipelines without for-loop spaghetti",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 3, "topic": "Copy vs Reference",
     "focus": "Avoid silent bugs from shared references in pipelines",
     "why": "One mutated batch shouldn't corrupt another",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 4, "topic": "Config with Dicts",
     "focus": "PipelineConfig — key-value storage, O(1) lookups, nested access",
     "why": "LLM API responses come back as nested JSON",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 5, "topic": "Deep JSON Parsing",
     "focus": ".get(), recursive flatten, safe navigation",
     "why": "Pull fields out of model output instantly + safely",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 6, "topic": "Big O Profiling",
     "focus": "Profile your own pipeline; O(1) vs O(n) vs O(n²)",
     "why": "Bad preprocessing freezes on thousands of records",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 2, "day": 7, "topic": "Big O Rewrite",
     "focus": "Rewrite O(n²) → O(n) in your collection code",
     "why": "Make your data pipeline scale to production",
     "path": "src/documind/operations/",
     "test": "tests/",
     "quiz": "quizzes/"},
    # ═══════════════════════════════════════════════════════════════
    # Week 3 — Complex Structures for AI Agents
    # ═══════════════════════════════════════════════════════════════
    {"week": 3, "day": 1, "topic": "Processing Queue",
     "focus": "FIFO queue for managing document backlogs",
     "why": "Conversation history buffers; queuing API requests",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 2, "topic": "Priority Queue",
     "focus": "Urgent documents processed first via heapq",
     "why": "Priority-based request scheduling in API backends",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 3, "topic": "Tree Traversal",
     "focus": "Document category hierarchy; DFS/BFS",
     "why": "Stepping through data hierarchies",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 4, "topic": "Pipeline Routing (Graph)",
     "focus": "Directed graph — multi-stage document routing",
     "why": "Multi-agent flows route an LLM through a graph of choices",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 5, "topic": "Decision Graph",
     "focus": "Conditional node-to-node document routing",
     "why": "Deterministic agent behavior through decision trees",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 6, "topic": "State Machine",
     "focus": "Pipeline stage transitions for document lifecycle",
     "why": "Controlling what an agent is allowed to do next",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 3, "day": 7, "topic": "Orchestrator Ship",
     "focus": "Full Orchestrator — combine queue + graph + state machine",
     "why": "End-to-end agent pipeline preparation",
     "path": "src/documind/orchestration/",
     "test": "tests/",
     "quiz": "quizzes/"},
    # ═══════════════════════════════════════════════════════════════
    # Week 4 — FastAPI Capstone
    # ═══════════════════════════════════════════════════════════════
    {"week": 4, "day": 1, "topic": "FastAPI Scaffold",
     "focus": "App setup + dependency injection + repo structure",
     "why": "Production backend scaffold",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 2, "topic": "POST /ingest",
     "focus": "Receive document array via endpoint",
     "why": "API ingest pattern — the entry point",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 3, "topic": "Validate & Clean",
     "focus": "Big O aware validation loop on incoming data",
     "why": "Don't let O(n²) blow up on the API endpoint",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 4, "topic": "Store Results",
     "focus": "Dict-backed result storage with O(1) lookups",
     "why": "Organized, fast-access output store",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 5, "topic": "API Harness Integration",
     "focus": "End-to-end: ingest → validate → store → respond",
     "why": "Complete deterministic AI pipeline",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 6, "topic": "Polish",
     "focus": "Error handling, structured logging, type hints everywhere",
     "why": "Make the repo look production-grade",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
    {"week": 4, "day": 7, "topic": "Ship",
     "focus": "Final commit, README, demo, review weak topics",
     "why": "Public proof of work for international eyes",
     "path": "src/documind/api/",
     "test": "tests/",
     "quiz": "quizzes/"},
]


def get_day_info() -> dict | None:
    """Return the curriculum entry for today, or None if before/after."""
    today = date.today()
    if today < START_DATE:
        return None
    delta = (today - START_DATE).days
    if delta >= len(CURRICULUM):
        return None  # Finished
    return CURRICULUM[delta]


def main() -> None:
    info = get_day_info()
    today = date.today()

    box = "▎"
    green = ""
    reset = ""
    if os.isatty(sys.stdout.fileno()):
        try:
            green = "\033[38;5;83m"
            reset = "\033[0m"
        except Exception:
            pass

    if info is None:
        if today < START_DATE:
            days_until = (START_DATE - today).days
            print(f"{box} DOCUMIND — AI Document Processing Pipeline")
            print(f"{box}")
            print(f"{box} ⏳ The grind starts on {START_DATE} ({days_until} days away).")
            print(f"{box}    Repo: https://github.com/anastanvir/dsa-oop-harness")
            print(f"{box}")
            print(f"{box} Get ready. Review CURRICULUM.md for the plan.")
        else:
            print(f"{box} DOCUMIND — AI Document Processing Pipeline")
            print(f"{box}")
            print(f"{box} ✓ All 28 days complete!")
            print(f"{box}   Review the capstone: https://github.com/anastanvir/dsa-oop-harness")
        return

    w, d = info["week"], info["day"]
    progress = (today - START_DATE).days + 1
    total = len(CURRICULUM)
    bar_len = 20
    filled = int(bar_len * progress / total)
    bar = "█" * filled + "░" * (bar_len - filled)

    print(f"{green}{box} DOCUMIND — DAY {progress}/{total}{reset}")
    print(f"{green}{box} Week {w} · Day {d}  |  {info['topic']}{reset}")
    print(f"{green}{box} ─────────────────────────────────────{reset}")
    print(f"{green}{box}{reset}")
    print(f"{green}{box} {bar}  {progress}/{total}{reset}")
    print(f"{green}{box}{reset}")
    print(f"{green}{box} Focus: {info['focus']}{reset}")
    print(f"{green}{box} Why:   {info['why']}{reset}")
    print(f"{green}{box}{reset}")
    print(f"{green}{box} 📄 Edit → {info['path']}{reset}")
    print(f"{green}{box} 🧪 Test → pytest {info['test']} -v{reset}")
    print(f"{green}{box} 📝 Quiz → {info.get('quiz', 'N/A')}{reset}")
    print(f"{green}{box} 📦 Repo → https://github.com/anastanvir/dsa-oop-harness{reset}")
    print(f"{green}{box}{reset}")
    print(f"{green}{box} THE RULES:{reset}")
    print(f"{green}{box}  • Write every line yourself — zero AI assistance{reset}")
    print(f"{green}{box}  • All tests green → day complete → git commit{reset}")
    print(f"{green}{box}  • Quiz first → code second → test third{reset}")
    print(f"{green}{box}  • Confidence ≤3? Mark it for review at week end{reset}")
    print(f"{green}{box}  • Stuck >30 min? Log blocker in NOTES.md, move on{reset}")
    print(f"{green}{box}{reset}")
    print(f"{green}{box} Today's mission: {info['focus']}{reset}")
    print(f"{green}{box} 🚀{reset}")


if __name__ == "__main__":
    main()
