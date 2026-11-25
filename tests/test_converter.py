"""Tests for the converter."""

import unittest
from src.converter import convert

RATES = {"CZK": (1, 1.0), "EUR": (1, 24.335), "JPY": (100, 15.812)}

class TestConvert(unittest.TestCase):

    def test_jpy_to_czk(self):
        result = convert(5000, "JPY", "CZK", RATES)
        self.assertEqual(result, 790.6)

    def test_same_currency(self):
        result = convert(100, "EUR", "EUR", RATES)
        self.assertEqual(result, 100)

    def test_EUR_to_JPY(self):
        result = convert(100, "EUR", "JPY", RATES)
        self.assertEqual(result, 15390.21)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            convert(-10, "EUR", "CZK", RATES)

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            convert(0, "EUR", "CZK", RATES)

    def test_unknown_currency(self):
        with self.assertRaises(ValueError):
            convert(100, "XYZ", "CZK", RATES)
        with self.assertRaises(ValueError):
            convert(100, "EUR", "XYZ", RATES)
