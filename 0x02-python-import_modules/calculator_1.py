#!/usr/bin/python3

def add(a, b):
    """Return the sum of two integers."""
    return a + b

def sub(a, b):
    """Return the difference of two integers."""
    return a - b

def mul(a, b):
    """Return the product of two integers."""
    return a * b

def div(a, b):
    """Return the result of integer division of two integers."""
    if b != 0:
        return a // b
    else:
        raise ValueError("Cannot divide by zero.")

if __name__ == "__main__":

    x = 10
    y = 2

    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {sub(x, y)}")
    print(f"Multiplication: {x} * {y} = {mul(x, y)}")

    try:
        print(f"Division: {x} / {y} = {div(x, y)}")
    except ValueError as e:
        print(f"Error: {e}")
