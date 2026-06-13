"""Tests for Day 7 — Factory Pattern & Polymorphism."""

from __future__ import annotations

from src.documind.core.processors import (
    BaseDocument,
    CSVDocument,
    DocumentFactory,
    JSONDocument,
    JSONValidator,
    TextDocument,
    TextValidator,
    chain_process,
)


class TestDocumentFactory:
    """Tests for DocumentFactory — polymorphic document creation."""

    def test_create_text(self) -> None:
        doc = DocumentFactory.create('text', 'hello')
        assert isinstance(doc, TextDocument)
        assert doc.process() == 'HELLO'

    def test_create_json(self) -> None:
        doc = DocumentFactory.create('json', '{"a": 1}')
        assert isinstance(doc, JSONDocument)

    def test_create_csv(self) -> None:
        doc = DocumentFactory.create('csv', 'a,b\n1,2')
        assert isinstance(doc, CSVDocument)
        assert doc.process() == 'a,b\n1,2'

    def test_create_text_validator(self) -> None:
        doc = DocumentFactory.create('text_validator', 'hello')
        assert isinstance(doc, TextValidator)
        assert doc.validate() is True

    def test_create_json_validator(self) -> None:
        doc = DocumentFactory.create('json_validator', '{"a": 1}')
        assert isinstance(doc, JSONValidator)
        assert doc.validate() is True

    def test_create_unknown_type_raises(self) -> None:
        try:
            DocumentFactory.create('unknown', 'data')
            assert False, 'Should have raised ValueError'
        except ValueError:
            pass

    def test_create_returns_concrete(self) -> None:
        doc = DocumentFactory.create('text', 'data')
        assert not isinstance(doc, BaseDocument.__class__)  # not abstract

    def test_all_created_share_base(self) -> None:
        for doc_type in DocumentFactory.list_types():
            content = 'test'
            if doc_type in ('json', 'json_validator'):
                content = '{"a": 1}'
            doc = DocumentFactory.create(doc_type, content)
            assert isinstance(doc, BaseDocument)

    def test_create_passes_content_only(self) -> None:
        """Factory create only passes content, no source."""
        doc = DocumentFactory.create('text', 'hello')
        assert doc.content == 'hello'
        assert doc.source == ''


class TestListTypes:
    """Tests for DocumentFactory.list_types() classmethod."""

    def test_list_types_returns_list(self) -> None:
        types = DocumentFactory.list_types()
        assert isinstance(types, list)

    def test_list_types_contains_expected(self) -> None:
        types = DocumentFactory.list_types()
        assert 'text' in types
        assert 'json' in types
        assert 'csv' in types
        assert 'text_validator' in types
        assert 'json_validator' in types

    def test_list_types_unique(self) -> None:
        types = DocumentFactory.list_types()
        assert len(types) == len(set(types))

    def test_list_types_is_classmethod(self) -> None:
        """Can be called on both class and instance."""
        assert DocumentFactory.list_types() == DocumentFactory().list_types()


class TestChainProcess:
    """Tests for chain_process — polymorphic batch processing."""

    def test_chain_single_doc(self) -> None:
        docs: list[BaseDocument] = [TextDocument('hello')]
        result = chain_process(docs)
        assert result == ['HELLO']

    def test_chain_multiple_types(self) -> None:
        docs = [
            TextDocument('hello'),
            JSONDocument('{"a": 1}'),
            CSVDocument('name,age\nAlice,30\n'),
        ]
        result = chain_process(docs)
        assert len(result) == 3
        assert result[0] == 'HELLO'
        assert '{\n  "a": 1\n}' in result[1] or '"a": 1' in result[1]
        assert result[2] == 'name,age\nAlice,30'

    def test_chain_preserves_order(self) -> None:
        docs: list[BaseDocument] = [
            TextDocument('first'),
            TextDocument('second'),
            TextDocument('third'),
        ]
        result = chain_process(docs)
        assert result == ['FIRST', 'SECOND', 'THIRD']

    def test_chain_empty_list(self) -> None:
        result = chain_process([])
        assert result == []

    def test_chain_with_factory_docs(self) -> None:
        """chain_process works with factory-created documents (polymorphism)."""
        docs = [
            DocumentFactory.create('text', 'hello'),
            DocumentFactory.create('csv', 'a,b\n1,2'),
        ]
        result = chain_process(docs)
        assert result[0] == 'HELLO'
        assert result[1] == 'a,b\n1,2'

    def test_chain_with_sanitized(self) -> None:
        from src.documind.core.processors import SanitizedDocument

        docs: list[BaseDocument] = [SanitizedDocument('  Hello  ')]
        result = chain_process(docs)
        assert result == ['hello']

    def test_chain_mixed_hierarchy(self) -> None:
        """Polymorphism: chain_process calls the right process() for each type."""
        docs: list[BaseDocument] = [
            TextDocument('A'),
            JSONDocument('{"b": 2}'),
            CSVDocument('x,y\n3,4'),
        ]
        results = chain_process(docs)
        assert results[0] == 'A'
        assert 'b' in results[1]
        assert '3,4' in results[2]
