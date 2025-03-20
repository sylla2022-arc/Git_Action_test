from src.math_operations import add, sub

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub():
    assert sub(1, 2) == -1
    assert sub(0, 0) == 0
    assert sub(-1, 1) == -2