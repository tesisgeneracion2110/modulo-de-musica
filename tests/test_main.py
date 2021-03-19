import sample.main
import pytest


def test_index():
    assert sample.main.index() == "Hello, world!"
