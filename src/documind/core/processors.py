"""Document processor hierarchy — Days 5-7: inheritance, overriding, factory pattern.

Builds on DocuMind document concepts with a hierarchy of processors:
- Day 5: Abstract base class with TextDocument, JSONDocument, CSVDocument
- Day 6: SanitizedDocument with overriding and validation mixins
- Day 7: DocumentFactory and chain_process for polymorphic processing
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any, ClassVar, Dict, List, Type


# ═══════════════════════════════════════════════════════════════════════════════
# DAY 5: Inheritance & Base Classes
# ═══════════════════════════════════════════════════════════════════════════════


class BaseDocument(ABC):
    """Abstract base document. Defines the common interface for all processors."""

    def __init__(self, content: str, source: str = '') -> None:
        # TODO: Store content and source
        self.content = content
        self.source = source

    @abstractmethod
    def process(self) -> str:
        # TODO: Subclasses must implement process()
        ...

    def summary(self) -> str:
        # TODO: Return a human-readable summary string
        return f'{type(self).__name__}: {len(self.content)} chars from {self.source}'


class TextDocument(BaseDocument):
    """Processes text content by uppercasing."""

    def process(self) -> str:
        # TODO: Return the content in uppercase
        return self.content.upper()


class JSONDocument(BaseDocument):
    """Processes JSON content by pretty-printing."""

    def __init__(self, content: str, source: str = '') -> None:
        # TODO: Call super().__init__ then parse self._data from content
        super().__init__(content, source)
        self._data: Any = json.loads(content)

    def process(self) -> str:
        # TODO: Return pretty-printed JSON
        return json.dumps(self._data, indent=2)


class CSVDocument(BaseDocument):
    """Processes CSV content: returns header + first data row."""

    def process(self) -> str:
        # TODO: Return first row (header) and second row (first data row)
        lines = self.content.splitlines()
        if not lines:
            return ''
        header = lines[0]
        data_row = lines[1] if len(lines) > 1 else ''
        return f'{header}\n{data_row}'


# ═══════════════════════════════════════════════════════════════════════════════
# DAY 6: Method Overriding & Validation
# ═══════════════════════════════════════════════════════════════════════════════


class SanitizedDocument(BaseDocument):
    """Overrides process() to strip whitespace and lowercase. Adds validate()."""

    def process(self) -> str:
        # TODO: Strip whitespace and lowercase the content
        return self.content.strip().lower()

    def validate(self) -> bool:
        # TODO: Must be overridden by subclasses
        ...


class TextValidator(SanitizedDocument):
    """Validates that text content is non-empty."""

    def validate(self) -> bool:
        # TODO: Return True if content is not empty after stripping
        return bool(self.content.strip())


class JSONValidator(SanitizedDocument):
    """Validates that content is parseable JSON."""

    def validate(self) -> bool:
        # TODO: Try to parse content as JSON, return True on success
        try:
            json.loads(self.content)
            return True
        except (json.JSONDecodeError, ValueError):
            return False


# ═══════════════════════════════════════════════════════════════════════════════
# DAY 7: Factory Pattern & Polymorphism
# ═══════════════════════════════════════════════════════════════════════════════


class DocumentFactory:
    """Factory for creating document processors by type name."""

    _registry: ClassVar[Dict[str, Type[BaseDocument]]] = {
        'text': TextDocument,
        'json': JSONDocument,
        'csv': CSVDocument,
        'text_validator': TextValidator,
        'json_validator': JSONValidator,
    }

    @classmethod
    def create(cls, doc_type: str, content: str) -> BaseDocument:
        # TODO: Look up doc_type in _registry and instantiate
        if doc_type not in cls._registry:
            raise ValueError(f'Unknown document type: {doc_type}')
        return cls._registry[doc_type](content)

    @classmethod
    def list_types(cls) -> List[str]:
        # TODO: Return all registered type names
        return list(cls._registry.keys())


def chain_process(docs: List[BaseDocument]) -> List[str]:
    # TODO: Call process() on each document and collect results
    return [doc.process() for doc in docs]
