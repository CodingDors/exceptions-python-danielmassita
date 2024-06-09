import pytest
from exercise import add, subtract, multiply, divide

# Tests
def test_add_valid_numbers():
    assert add("3", "2") == 5.0

def test_add_invalid_numbers():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid numbers."):
        add("abc", "2")

def test_subtract_valid_numbers():
    assert subtract("5", "3") == 2.0

def test_subtract_invalid_numbers():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid numbers."):
        subtract("5", "abc")

def test_multiply_valid_numbers():
    assert multiply("4", "3") == 12.0

def test_multiply_invalid_numbers():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid numbers."):
        multiply("abc", "3")

def test_divide_valid_numbers():
    assert divide("8", "4") == 2.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide("8", "0")

def test_divide_invalid_numbers():
    with pytest.raises(ValueError, match="Invalid input. Please provide valid numbers."):
        divide("abc", "4")
