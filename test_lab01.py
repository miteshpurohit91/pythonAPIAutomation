import pytest


def test_sub():
    assert 2 - 2 == 1


@pytest.mark.smoke
def test_sum():
    assert 2 + 2 == 4
