"""Tests for the converter."""

import unittest
from src.converter import convert

RATES = {"CZK": (1, 1.0), "EUR": (1, 24.335), "JPY": (100, 15.812)}

class TestConvert(unittest.TestCase):

    def test_jpy_to_czk(self):
        result = convert(5000, "JPY", "CZK", RATES)
        self.assertEqual(result, 790.6)