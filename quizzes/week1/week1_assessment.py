"""Week 1 Comprehensive Assessment — OOP Foundations in DocuMind.

Each function q1() through q10() returns a string answer.
Covers: self, __init__, class vs instance attrs, __repr__, __str__,
__call__, context managers, inheritance, super(), abstract classes, factory.
"""

from __future__ import annotations


def q1() -> str:
    """What is the first parameter of every instance method in Python?"""
    # TODO: Return the parameter name
    return 'self'


def q2() -> str:
    """Which method is the constructor (initializer) in a Python class?"""
    # TODO: Return the method name with double underscores
    return '__init__'


def q3() -> str:
    """If a value is defined directly in the class body (not in __init__), is it a class or instance attribute?"""
    # TODO: Return 'class' or 'instance'
    return 'class'


def q4() -> str:
    """Which dunder method returns an unambiguous developer-readable string for an object?"""
    # TODO: Return the method name with double underscores
    return '__repr__'


def q5() -> str:
    """Which dunder method returns a user-friendly string when you print() an object?"""
    # TODO: Return the method name with double underscores
    return '__str__'


def q6() -> str:
    """Which dunder method makes an instance callable like a function?"""
    # TODO: Return the method name with double underscores
    return '__call__'


def q7() -> str:
    """Which two dunder methods implement the context manager protocol (enter/exit)?"""
    # TODO: Return them separated by a comma and space
    return '__enter__, __exit__'


def q8() -> str:
    """Which function do you call to invoke a parent class method from a child class?"""
    # TODO: Return the function name
    return 'super'


def q9() -> str:
    """What Python built-in module provides ABC and abstractmethod?"""
    # TODO: Return the module name
    return 'abc'


def q10() -> str:
    """What design pattern provides an interface for creating objects without specifying their concrete classes?"""
    # TODO: Return the pattern name
    return 'factory'
