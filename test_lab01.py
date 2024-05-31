import pytest


def test_sub():
    assert 2 - 2 == 1


@pytest.mark.smoke
def test_sum():
    assert 2 + 2 == 4


@pytest.mark.skip(reason="Not Implemented yet")
def test_sum2():
    assert 3 + 3 == 6
