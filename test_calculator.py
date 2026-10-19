import pytest
from calculator import add, subtract, multiply, divide

# HOW A TEST WORKS
#   1. The function name MUST start with `test_` so pytest finds it.
#   2. Call your code with some input.
#   3. `assert` what the answer should be. If the assert is False, the test fails.
#
# Run all tests:   pytest
# Run with detail: pytest -v


# SAMPLE TEST (done for you)
def test_add():
    assert add(2, 3) == 5          # normal case
    assert add(-2, -3) == -5       # negative numbers
    assert add(-4, 10) == 6        # mixed signs
    assert add(0, 0) == 0          # zero
    assert add(2.5, 0.5) == 3.0    # decimals


# YOUR TURN
# Write the tests below. Follow the same pattern as test_add.


# TODO: write test_subtract()
def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-3, -10) == 7
    assert subtract(3, -5) == 8
    assert subtract(0, 0) == 0
    assert subtract(1, 0) == 1
    assert subtract(1.7, -2.1) == 3.8


# TODO: write test_multiply()
def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 5) == 0
    assert multiply(1, 3.7) == 3.7
    assert multiply(-10, 5) == -50
    assert multiply(-4, -5) == 20
    assert multiply(1.5, -1.5) == -2.25


# TODO: write test_divide()
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(-10, -1) == 10
    assert divide(5, .5) == 10
    assert divide(1.5, -.5) == -3


# TODO: write test_divide_by_zero()
#   divide() raises a ValueError when b is 0. Here's how to test for an error:
#       with pytest.raises(ValueError):
#           divide(1, 0)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


# BONUS: add any extra tests you want!
