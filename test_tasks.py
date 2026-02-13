import pytest
import sys
import os
from io import StringIO
from unittest.mock import patch


# =============================================================================
# TASK 1 TESTS: Code Errors (no input)
# =============================================================================

def test_task1_00_file_exists():
    """Test that task1.py exists"""
    assert os.path.exists('task1.py'), "task1.py not found"


def test_task1_01_snippet_1_fixed():
    """Snippet 1: Variable name case error (Name vs name)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
name = "Alex"
age = 15
print(f"Hello, {name}!")
print(f"You are {age} years old.")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Hello, Alex!" in output, "Snippet 1 not fixed correctly"


def test_task1_02_snippet_2_fixed():
    """Snippet 2: Cannot concatenate string and int"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
cats = 3
dogs = 2
total = cats + dogs
print(f"Total pets: {total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Total pets: 5" in output, "Snippet 2 not fixed correctly"


def test_task1_03_snippet_3_fixed():
    """Snippet 3: Variable name typo (heigth vs height)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
width = 8
height = 5
print(f"Width: {width}, Height: {height}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Height: 5" in output, "Snippet 3 not fixed correctly"


def test_task1_04_snippet_4_fixed():
    """Snippet 4: Missing curly braces in f-string"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
price = 19.99
print(f"The price is: ${price}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "19.99" in output, "Snippet 4 not fixed correctly"


def test_task1_05_snippet_5_fixed():
    """Snippet 5: Cannot concatenate string and float"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
pizzas = 3
slices_per_pizza = 8
people = 8
total_slices = pizzas * slices_per_pizza
slices_each = total_slices / people
print(f"Total slices: {total_slices}")
print(f"Slices per person: {slices_each}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Total slices: 24" in output, "Snippet 5 not fixed correctly"
    assert "Slices per person: 3" in output, "Snippet 5 not fixed correctly"


def test_task1_06_snippet_6_fixed():
    """Snippet 6: Variable name case error (book_Title vs book_title)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
book_title = "Python Basics"
price = 12.99
quantity = 3
total = price * quantity
print(f"Book: {book_title}")
print(f"Total: ${total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Book: Python Basics" in output, "Snippet 6 not fixed correctly"
    assert "38.97" in output, "Snippet 6 not fixed correctly"


# =============================================================================
# TASK 2 TESTS: Input and Data Conversion Errors
# =============================================================================

def test_task2_00_file_exists():
    """Test that task2.py exists"""
    assert os.path.exists('task2.py'), "task2.py not found"


def test_task2_01_program_1_fixed():
    """Program 1: Missing int() conversion for tickets"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "Total cost: $48" in output, "Program 1 not fixed correctly - 4 tickets at $12 should be $48"


def test_task2_02_program_2_fixed():
    """Program 2: Missing int() conversion for both numbers"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "= 42" in output, "Program 2 not fixed correctly - 25 + 17 should be 42, not 2517"


def test_task2_03_program_3_fixed():
    """Program 3: Missing float() conversion for celsius"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "77" in output, "Program 3 not fixed correctly - 25 Celsius should be 77 Fahrenheit"


def test_task2_04_program_4_fixed():
    """Program 4: Missing float() conversion for hours and rate"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "620" in output, "Program 4 not fixed correctly - 40 hours at $15.50 should be $620"


def test_task2_05_program_5_fixed():
    """Program 5: Should use float() instead of int() for decimal support"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "34" in output, "Program 5 not fixed correctly - 8.5 x 4 should be 34.0"


def test_task2_06_program_6_fixed():
    """Program 6: Missing float() conversion for tip_percent"""
    from task2 import main
    
    inputs = iter(['4', '25', '17', '25', '40', '15.50', '8.5', '4', '45.50', '20'])
    with patch('builtins.input', lambda prompt: next(inputs)):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            main()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "54.6" in output, "Program 6 not fixed correctly - $45.50 + 20% tip should be $54.60"
