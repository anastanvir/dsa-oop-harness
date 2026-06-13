from __future__ import annotations

import json
from typing import Any


# === DAY 1: Classes & self ===

class Document:
    """A document in the DocuMind pipeline. Grows across Days 1–4."""

    # --- Day 2: Class attributes ---
    # TODO: counter = 0
    # TODO: allowed_types = ['text', 'json', 'csv', 'markdown']

    def __init__(
        self,
        content: str,
        doc_type: str = 'text',
        metadata: dict | None = None,
    ) -> None:
        # TODO: Store self.content, self.doc_type, self.metadata (default {})
        # TODO: Increment Document.counter
        pass

    def char_count(self) -> int:
        # TODO: Return len(self.content)
        pass

    def word_count(self) -> int:
        # TODO: Return len(self.content.split())
        pass

    # === DAY 2: Class vs Instance Attributes ===

    @classmethod
    def from_json(cls, json_str: str) -> Document:
        # TODO: Parse JSON string and return a Document with the parsed content
        pass

    @classmethod
    def allowed(cls) -> list[str]:
        # TODO: Return the class-level allowed_types list
        pass

    @property
    def size_kb(self) -> float:
        # TODO: Return len(self.content) / 1024
        pass

    # === DAY 3: Dunder Methods ===

    def __repr__(self) -> str:
        # TODO: Return 'Document(type={doc_type}, chars={n})'
        pass

    def __str__(self) -> str:
        # TODO: Return first 80 characters of content + '...'
        pass

    def __len__(self) -> int:
        # TODO: Return len(self.content)
        pass

    def __eq__(self, other: object) -> bool:
        # TODO: Compare self.content and self.doc_type with other's
        pass

    # === DAY 4: Callable, Context Manager, Operator Overloading ===

    def __call__(self, prefix: str = '') -> str:
        # TODO: Return prefix + self.content
        pass

    def __enter__(self) -> Document:
        # TODO: Print 'Entered document context.' and return self
        pass

    def __exit__(self, *args: Any) -> None:
        # TODO: Print 'Exited document context.'
        # No special cleanup needed
        pass

    def __add__(self, other: Document) -> Document:
        # TODO: Return a new Document with concatenated content (same doc_type)
        pass
