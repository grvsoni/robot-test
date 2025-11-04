"""
Simple Calculator Application
A basic calculator with add, subtract, multiply, and divide operations.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b and return the result.
        
        Args:
            a: The numerator
            b: The denominator
            
        Returns:
            The result of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
