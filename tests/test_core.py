import pytest

from fibonacci_kata.core import fibonacci


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (6, 8), (10, 55)])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize("n", [1000, 10**4, 10**5, 10**6, 10**7])
def test_fibonacci_huge_numbers(n):
    assert fibonacci(n) > 0
