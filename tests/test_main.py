import sample.main
import pytest


def test_index():
    assert sample.main.index() == "Hello, world!"


@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (6, 6, 12)
])
def test_add(x, y, result):
    assert sample.main.add(x, y) == result

