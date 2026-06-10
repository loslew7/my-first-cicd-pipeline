"""
Simple application for CI/CD pipeline demonstration.
Contains basic functions for greeting and math operations.
"""

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(greet("DevOps Engineer"))
    print(f"2 + 2 = {add(2, 2)}")
    print(f"10 / 2 = {divide(10, 2)}")
