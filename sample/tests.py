from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):
    """tests for Calc file"""
    def test_add_number(self):
        self.assertEqual(add(1, 3), 4)
