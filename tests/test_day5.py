"""Tests for Day 5 — Inheritance & Base Classes."""

from __future__ import annotations

import json

from src.documind.core.processors import (
    BaseDocument,
    CSVDocument,
    JSONDocument,
    TextDocument,
)


class TestBaseDocument:
    """Tests for the abstract BaseDocument class."""

    def test_cannot_instantiate_abstract(self) -> None:
        """BaseDocument is abstract and cannot be instantiated directly."""
        try:
            BaseDocument('hello')  # type: ignore
            assert False, 'Should have raised TypeError'
        except TypeError:
            pass

    def test_concrete_subclass_instantiation(self) -> None:
        """TextDocument is concrete and can be instantiated."""
        doc = TextDocument('hello', source='test')
        assert doc is not None
        assert isinstance(doc, BaseDocument)

    def test_summary_format(self) -> None:
        """summary() returns correct format."""
        doc = TextDocument('abc', source='notes.txt')
        expected = 'TextDocument: 3 chars from notes.txt'
        assert doc.summary() == expected

    def test_summary_default_source(self) -> None:
        """summary() works with default empty source."""
        doc = TextDocument('data')
        assert '4 chars from ' in doc.summary()


class TestTextDocument:
    """Tests for TextDocument — uppercasing processor."""

    def test_process_uppercases(self) -> None:
        doc = TextDocument('hello world')
        assert doc.process() == 'HELLO WORLD'

    def test_process_with_mixed_case(self) -> None:
        doc = TextDocument('Hello World!')
        assert doc.process() == 'HELLO WORLD!'

    def test_process_empty_string(self) -> None:
        doc = TextDocument('')
        assert doc.process() == ''

    def test_process_with_numbers(self) -> None:
        doc = TextDocument('abc123')
        assert doc.process() == 'ABC123'


class TestJSONDocument:
    """Tests for JSONDocument — pretty-printing processor."""

    def test_process_pretty_print(self) -> None:
        doc = JSONDocument('{"a": 1, "b": 2}')
        expected = json.dumps({'a': 1, 'b': 2}, indent=2)
        assert doc.process() == expected

    def test_process_nested(self) -> None:
        content = '{"x": {"y": [1, 2, 3]}}'
        doc = JSONDocument(content)
        expected = json.dumps({'x': {'y': [1, 2, 3]}}, indent=2)
        assert doc.process() == expected

    def test_parses_on_init(self) -> None:
        doc = JSONDocument('{"key": "value"}')
        assert doc._data == {'key': 'value'}

    def test_invalid_json_raises(self) -> None:
        try:
            JSONDocument('not-json')
            assert False, 'Should have raised json.JSONDecodeError'
        except json.JSONDecodeError:
            pass

    def test_summary_from_json(self) -> None:
        doc = JSONDocument('{"a": 1}', source='config.json')
        assert 'JSONDocument' in doc.summary()
        assert 'config.json' in doc.summary()


class TestCSVDocument:
    """Tests for CSVDocument — header + first data row processor."""

    def test_process_returns_header_and_first_row(self) -> None:
        csv_data = 'name,age\nAlice,30\nBob,25\n'
        doc = CSVDocument(csv_data)
        assert doc.process() == 'name,age\nAlice,30'

    def test_process_single_row(self) -> None:
        csv_data = 'header_only\n'
        doc = CSVDocument(csv_data)
        assert doc.process() == 'header_only\n'

    def test_process_empty(self) -> None:
        doc = CSVDocument('')
        assert doc.process() == ''

    def test_process_multiple_rows(self) -> None:
        csv_data = 'col1,col2\nr1c1,r1c2\nr2c1,r2c2\nr3c1,r3c2\n'
        doc = CSVDocument(csv_data)
        assert doc.process() == 'col1,col2\nr1c1,r1c2'


class TestInheritanceHierarchy:
    """Tests for the class hierarchy relationships."""

    def test_textdocument_is_subclass(self) -> None:
        assert issubclass(TextDocument, BaseDocument)

    def test_jsondocument_is_subclass(self) -> None:
        assert issubclass(JSONDocument, BaseDocument)

    def test_csvdocument_is_subclass(self) -> None:
        assert issubclass(CSVDocument, BaseDocument)

    def test_all_share_base(self) -> None:
        for cls in (TextDocument, JSONDocument, CSVDocument):
            content = '{"a": 1}' if cls is JSONDocument else ''
            assert isinstance(cls(content, source='test'), BaseDocument)
