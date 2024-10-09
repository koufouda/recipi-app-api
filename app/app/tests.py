"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(-2, 789)

        self.assertEqual(res, 787)

    def test_subtract_numbers(self):
        """Test substract numbers together"""
        res = calc.subtract(-2, 789)

        self.assertEqual(res, -791)
        self.assertNotEquals(res, -790)