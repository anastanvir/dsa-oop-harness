from __future__ import annotations

"""Tests for Day 4 — __call__, context manager, __add__."""

from src.documind.core.document import Document


def test_call_with_prefix() -> None:
    """__call__ returns prefix + content."""
    doc = Document('World')
    result = doc('Hello ')
    assert result == 'Hello World'


def test_call_default_prefix() -> None:
    """__call__ with no prefix returns just the content."""
    doc = Document('Alone')
    assert doc() == 'Alone'


def test_context_manager_prints_messages(capsys: object) -> None:
    """__enter__ and __exit__ print context manager messages."""
    doc = Document('test')
    with doc as d:
        assert d is doc  # __enter__ returns self

    captured = capsys.readouterr()  # type: ignore
    out = captured.out
    assert 'Entered' in out or 'entered' in out
    assert 'Exited' in out or 'exited' in out


def test_add_concatenates_content() -> None:
    """__add__ returns a new Document with concatenated content."""
    doc1 = Document('Hello ', 'text')
    doc2 = Document('World', 'text')
    result = doc1 + doc2
    assert isinstance(result, Document)
    assert result.content == 'Hello World'
    assert result.doc_type == 'text'


def test_add_keeps_same_doc_type() -> None:
    """__add__ preserves the doc_type of the left operand."""
    doc1 = Document('part1', 'markdown')
    doc2 = Document('part2', 'markdown')
    result = doc1 + doc2
    assert result.doc_type == 'markdown'


def test_add_does_not_mutate_originals() -> None:
    """__add__ should not mutate the original documents."""
    doc1 = Document('Hello ', 'text')
    doc2 = Document('World', 'text')
    doc1 + doc2
    assert doc1.content == 'Hello '
    assert doc2.content == 'World'
