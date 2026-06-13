from __future__ import annotations

"""Tests for Day 1 — Basic Document class instantiation and methods."""

from src.documind.core.document import Document


def test_document_instantiation() -> None:
    """Document can be instantiated with content, doc_type, and metadata."""
    doc = Document('Hello world', 'text', {'author': 'test'})
    assert doc.content == 'Hello world'
    assert doc.doc_type == 'text'
    assert doc.metadata == {'author': 'test'}


def test_char_count() -> None:
    """char_count() returns the length of the content string."""
    doc = Document('Hello world')
    assert doc.char_count() == 11


def test_word_count() -> None:
    """word_count() returns the number of words in the content."""
    doc = Document('Hello beautiful world')
    assert doc.word_count() == 3


def test_default_doc_type() -> None:
    """Default doc_type is 'text' when not provided."""
    doc = Document('Some content')
    assert doc.doc_type == 'text'


def test_default_metadata() -> None:
    """Metadata defaults to an empty dict (not None)."""
    doc = Document('Content')
    assert doc.metadata == {}
    assert doc.metadata is not None
