import pytest
from calculator import Calculator
from history import History

"""
Test module for Calculator class.
Ensures correctness of calculator operations and history functionality.
"""


@pytest.fixture
def clear_calc_history():
    """Fixture to clear calculation history before each test."""
    History.clear_history()


@pytest.mark.parametrize("a,b,expected", [(5, 3, 8), (-2, 4, 2), (0, 0, 0)])
def test_add(clear_calc_history, a, b, expected):
    """Test addition operation."""
    result = Calculator.add(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(5, 3, 2), (-2, 4, -6), (0, 0, 0)])
def test_subtract(clear_calc_history, a, b, expected):
    """Test subtraction operation."""
    result = Calculator.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(5, 3, 15), (-2, 4, -8), (0, 1, 0)])
def test_multiply(clear_calc_history, a, b, expected):
    """Test multiplication operation."""
    result = Calculator.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [(6, 3, 2), (-8, 4, -2), (5, 2, 2.5)])
def test_divide(clear_calc_history, a, b, expected):
    """Test division operation."""
    result = Calculator.divide(a, b)
    assert result == expected


def test_divide_by_zero(clear_calc_history):
    """Test division by zero throws ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)


def test_add_to_history(clear_calc_history):
    """Test adding calculation to history."""
    calc = Calculator.add_calculation_to_history('add', 1, 2)
    assert calc.result == 3
    assert len(History.get_history()) == 1