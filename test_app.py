import pytest
from app import greet, add, divide

def test_greet():
    """Test the greet function"""
    assert greet("World") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"

def test_add():
    """Test the add function"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 10 # WRONG! Should be 0

def test_divide():
    """Test the divide function"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    """Test that dividing by zero raises an error"""
    with pytest.raises(ValueError):
        divide(10, 0)
