from app.main import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5


def test_calculate_add():
    assert calculate(2, 3, "+") == 5


def test_calculate_subtract():
    assert calculate(5, 2, "-") == 3


def test_calculate_multiply():
    assert calculate(3, 3, "*") == 9


def test_calculate_divide():
    assert calculate(10, 2, "/") == 5
