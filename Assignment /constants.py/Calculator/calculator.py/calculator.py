# calculator.py

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x divided by y.
    
    Raises:
        ValueError: If y is zero (division by zero is not allowed).
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
