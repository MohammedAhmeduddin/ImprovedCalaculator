import pytest
from faker import Faker
from calculator import Calculator
from calculation import Calculation
from history import History

"""
Test module for Calculator class.
Ensures correctness of calculator operations and history functionality.
"""

# Initialize Faker
fake = Faker()

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

# Faker test for random data generation
@pytest.fixture
def fake_data():
    """Fixture to generate random input data using Faker."""
    return {
        "a": fake.random_int(min=1, max=100),
        "b": fake.random_int(min=1, max=100),
        "operation": fake.random_element(elements=('add', 'subtract', 'multiply', 'divide')),
    }

def test_with_faker(fake_data):
    """Test operations using random data from Faker."""
    a = fake_data["a"]
    b = fake_data["b"]
    operation = fake_data["operation"]
    
    # Dictionary dispatch method to map operations to functions
    operations = {
        'add': (Calculator.add, lambda a, b: a + b),
        'subtract': (Calculator.subtract, lambda a, b: a - b),
        'multiply': (Calculator.multiply, lambda a, b: a * b),
        'divide': (Calculator.divide, lambda a, b: a / b if b != 0 else pytest.raises(ZeroDivisionError))
    }

    # Select the appropriate function and expected result from the dictionary
    operation_func, expected_result = operations.get(operation)

    if operation == 'divide' and b == 0:
        with pytest.raises(ZeroDivisionError):
            operation_func(a, b)
    else:
        result = operation_func(a, b)
        assert result == expected_result(a, b)

def test_invalid_operation_in_calculator():
    """Test that an invalid operation raises a ValueError."""
    with pytest.raises(ValueError):
        Calculator.add_calculation_to_history('modulus', 5, 3)

def test_clear_history():
    """Test clearing history."""
    History.add_to_history(Calculation('add', 1, 2, 3))
    History.clear_history()
    assert len(History.get_history()) == 0

def test_get_last_calculation_empty():
    """Test getting the last calculation when history is empty."""
    History.clear_history()
    assert History.get_last_calculation() is None

def test_invalid_calculation_validation():
    """Test that non-numeric values raise a ValueError."""
    with pytest.raises(ValueError):
        Calculation('add', 'a', 2, 3)  # Invalid operand 'a'
    with pytest.raises(ValueError):
        Calculation('subtract', 2, 'b', 1)  # Invalid operand 'b'
    with pytest.raises(ValueError):
        Calculation('multiply', 2, 2, 'c')  # Invalid result 'c'


def test_calculation_equality():
    """Test equality comparison between Calculation instances."""
    calc1 = Calculation('add', 1, 2, 3)
    calc2 = Calculation('add', 1, 2, 3)
    calc3 = Calculation('subtract', 1, 2, -1)
    
    assert calc1 == calc2  # Should be equal
    assert calc1 != calc3  # Should not be equal



