"""Quiz for Day 6 — Abstract Classes, super(), Overriding.

Answer each question by returning the correct string from the function.
"""

from __future__ import annotations


def q1() -> str:
    """What function do you call to invoke a parent class method from a child?"""
    # TODO: Return the function name
    return 'super'


def q2() -> str:
    """What decorator marks a method as abstract in Python?"""
    # TODO: Return the decorator name without @
    return 'abstractmethod'


def q3() -> str:
    """Which class in DocuMind overrides process() to strip whitespace and lowercase?"""
    # TODO: Return the class name
    return 'SanitizedDocument'


def q4() -> str:
    """If a child class defines a method with the same name as the parent, what is this called?"""
    # TODO: Return the term
    return 'overriding'


def q5() -> str:
    """Which module must you import from to use ABC and abstractmethod?"""
    # TODO: Return the module path
    return 'abc'
