from __future__ import annotations

"""Tests for Day 2 — Class attributes, classmethods, properties."""

from src.documind.core.document import Document


def test_counter_starts_at_zero() -> None:
    """Document.counter starts at 0 and increments with each instantiation."""
    # Reset counter for test isolation
    Document.counter = 0

    d1 = Document('a')
    assert Document.counter == 1

    d2 = Document('b')
    assert Document.counter == 2

    d3 = Document('c')
    assert Document.counter == 3


def test_allowed_types_exists() -> None:
    """Document.allowed_types is a class-level list."""
    assert hasattr(Document, 'allowed_types')
    assert isinstance(Document.allowed_types, list)
    assert 'text' in Document.allowed_types
    assert 'json' in Document.allowed_types
    assert 'csv' in Document.allowed_types
    assert 'markdown' in Document.allowed_types


def test_from_json() -> None:
    """from_json() parses a JSON string and returns a Document."""
    json_str = '{"title": "test", "body": "hello"}'
    doc = Document.from_json(json_str)
    assert isinstance(doc, Document)
    # The content should be the parsed JSON represented as a string
    assert 'title' in doc.content
    assert 'test' in doc.content


def test_allowed_class_method() -> None:
    """allowed() classmethod returns the allowed_types list."""
    types = Document.allowed()
    assert types == Document.allowed_types


def test_size_kb_property() -> None:
    """size_kb returns a float value of len(content) / 1024."""
    doc = Document('A' * 2048)
    assert isinstance(doc.size_kb, float)
    assert doc.size_kb == 2.0  # 2048 / 1024


def test_default_metadata_with_new_instance() -> None:
    """Instantiating without metadata gives an empty dict."""
    doc = Document('hello')
    assert doc.metadata == {}
    assert doc.metadata is not None
