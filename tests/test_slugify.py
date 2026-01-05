import pytest

from slugify import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_characters():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_multiple_spaces():
    assert slugify("Hello    World") == "hello-world"


def test_slugify_leading_trailing_spaces():
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_numbers():
    assert slugify("Version 2.0") == "version-2-0"
