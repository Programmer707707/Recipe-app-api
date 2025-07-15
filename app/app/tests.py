"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """
    Checks the add method's functionality
    """
    def test_add_numbers(self):
        res = calc.add(5,6)
        
        self.assertEqual(res, 11)