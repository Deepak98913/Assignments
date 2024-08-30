# main.py

# Import functions from calculator.py
from calculator import add, subtract, multiply, divide

def test_calculator():
    x = 10
    y = 5
    
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    
    try:
        print(f"{x} / {y} = {divide(x, y)}")
        print(f"{x} / 0 = {divide(x, 0)}")  # This will raise an exception
    except ValueError as e:
        print(e)

# Call the test function
test_calculator()
