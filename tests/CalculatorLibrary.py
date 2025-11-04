"""
Robot Framework Library for Calculator Application
This library provides keywords to test the Calculator class.
"""

import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import Calculator


class CalculatorLibrary:
    """Robot Framework library for testing Calculator functionality."""
    
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        """Initialize the library with a Calculator instance."""
        self.calculator = Calculator()
    
    def add_numbers(self, a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return self.calculator.add(float(a), float(b))
    
    def subtract_numbers(self, a, b):
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return self.calculator.subtract(float(a), float(b))
    
    def multiply_numbers(self, a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return self.calculator.multiply(float(a), float(b))
    
    def divide_numbers(self, a, b):
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        return self.calculator.divide(float(a), float(b))
