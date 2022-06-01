import pytest


def func(x):
    return x + 1


def test_answer_negative():
    assert func(3) != 5


def test_answer_positive():
    assert func(3) == 4


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()