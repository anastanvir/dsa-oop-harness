from __future__ import annotations

"""Tests for Day 3 — Dunder methods: __repr__, __str__, __len__, __eq__."""

from src.documind.core.document import Document


def test_repr_format() -> None:
    """__repr__ returns 'Document(type={doc_type}, chars={n})'."""
    doc = Document('Hello world', 'markdown')
    expected = "Document(type=markdown, chars=11)"
    assert repr(doc) == expected


def test_str_truncation() -> None:
    """__str__ returns first 80 chars of content plus '...'."""
    long_content = 'A' * 100
    doc = Document(long_content)
    result = str(doc)
    assert result == ('A' * 80) + '...'
    assert len(result) == 83  # 80 chars + '...'


def test_str_short_content() -> None:
    """__str__ adds '...' even for short content (truncation at 80)."""
    doc = Document('Short')
    result = str(doc)
    assert result == 'Short...'
    assert len(result) == 9  # 5 + 3


def test_len_returns_content_length() -> None:
    """__len__ returns the length of the content string."""
    doc = Document('Python')
    assert len(doc) == 6


def test_eq_compares_content_and_type() -> None:
    """__eq__ compares both content and doc_type."""
    doc1 = Document('same content', 'json')
    doc2 = Document('same content', 'json')
    assert doc1 == doc2


def test_eq_different_content() -> None:
    """Documents with different content are not equal."""
    doc1 = Document('hello')
    doc2 = Document('world')
    assert doc1 != doc2


def test_eq_different_type() -> None:
    """Documents with same content but different type are not equal."""
    doc1 = Document('data', 'json')
    doc2 = Document('data', 'csv')
    assert doc1 != doc2
