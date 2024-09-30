import subprocess

def test_add():
    result = subprocess.run(["python", "main.py", "5", "3", "add"], capture_output=True, text=True)
    assert "The result of 5.0 add 3.0 is 8.0" in result.stdout

def test_divide_by_zero():
    result = subprocess.run(["python", "main.py", "1", "0", "divide"], capture_output=True, text=True)
    assert "An error occurred: Cannot divide by zero" in result.stdout

def test_invalid_input():
    result = subprocess.run(["python", "main.py", "a", "3", "add"], capture_output=True, text=True)
    assert "Invalid number input: 'a' is not a valid number." in result.stdout

def test_invalid_operation():
    result = subprocess.run(["python", "main.py", "5", "3", "modulus"], capture_output=True, text=True)
    assert "Unknown operation: modulus" in result.stdout

def test_mixed_invalid_input():
    result = subprocess.run(["python", "main.py", "7", "b", "subtract"], capture_output=True, text=True)
    assert "Invalid number input: 'b' is not a valid number." in result.stdout






