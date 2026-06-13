"""Tests for Day 6 — Method Overriding & Validation."""

from __future__ import annotations

import json

from src.documind.core.processors import (
    JSONValidator,
    SanitizedDocument,
    TextValidator,
)


class TestSanitizedDocument:
    """Tests for SanitizedDocument — overrides process() with strip + lowercase."""

    def test_process_strips_whitespace(self) -> None:
        doc = SanitizedDocument('  Hello World  ')
        assert doc.process() == 'hello world'

    def test_process_lowercases(self) -> None:
        doc = SanitizedDocument('HELLO')
        assert doc.process() == 'hello'

    def test_process_strips_and_lowercases(self) -> None:
        doc = SanitizedDocument('  ABC DEF  ')
        assert doc.process() == 'abc def'

    def test_process_empty_string(self) -> None:
        doc = SanitizedDocument('')
        assert doc.process() == ''

    def test_process_newlines_and_tabs(self) -> None:
        doc = SanitizedDocument('\tLine1\nLine2\t')
        assert doc.process() == 'line1\nline2'

    def test_validate_not_implemented(self) -> None:
        """SanitizedDocument.validate() is not overridden — should raise or return None."""
        doc = SanitizedDocument('hello')
        result = doc.validate()
        assert result is None or result is ...  # ... evaluates to Ellipsis


class TestTextValidator:
    """Tests for TextValidator — validates non-empty content."""

    def test_validate_non_empty(self) -> None:
        doc = TextValidator('hello')
        assert doc.validate() is True

    def test_validate_empty(self) -> None:
        doc = TextValidator('')
        assert doc.validate() is False

    def test_validate_whitespace_only(self) -> None:
        doc = TextValidator('   ')
        assert doc.validate() is False

    def test_process_still_strips_and_lowercases(self) -> None:
        doc = TextValidator('  Hello  ')
        assert doc.process() == 'hello'

    def test_inherits_sanitized_process(self) -> None:
        doc = TextValidator('TEST')
        assert doc.process() == 'test'


class TestJSONValidator:
    """Tests for JSONValidator — validates parseable JSON."""

    def test_validate_valid_json(self) -> None:
        doc = JSONValidator('{"a": 1}')
        assert doc.validate() is True

    def test_validate_valid_json_array(self) -> None:
        doc = JSONValidator('[1, 2, 3]')
        assert doc.validate() is True

    def test_validate_invalid_json(self) -> None:
        doc = JSONValidator('not json')
        assert doc.validate() is False

    def test_validate_empty_string(self) -> None:
        doc = JSONValidator('')
        assert doc.validate() is False

    def test_process_still_strips_and_lowercases(self) -> None:
        doc = JSONValidator('  {"A": 1}  ')
        assert doc.process() == '{"a": 1}'  # lowercased

    def test_validate_numeric_json(self) -> None:
        doc = JSONValidator('42')
        assert doc.validate() is True


class TestOverridingChain:
    """Tests for method resolution order and overriding."""

    def test_sanitized_overrides_process(self) -> None:
        """SanitizedDocument.process is different from TextDocument.process."""
        from src.documind.core.processors import TextDocument

        text_doc = TextDocument('  HELLO  ')
        sanitized_doc = SanitizedDocument('  HELLO  ')

        assert text_doc.process() == '  HELLO  '   # uppercased (already upper)
        assert sanitized_doc.process() == 'hello'  # stripped + lowered

    def test_validator_inherits_sanitized_process(self) -> None:
        """TextValidator and JSONValidator use SanitizedDocument's process, not BaseDocument's."""
        t = TextValidator('  ABC  ')
        j = JSONValidator('  {"X": 1}  ')
        assert t.process() == 'abc'
        assert j.process() == '{"x": 1}'
