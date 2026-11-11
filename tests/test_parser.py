
"""Tests for the CNB rates parser."""

import unittest
from src.parser import parse_rates

SAMPLE = """04 Nov 2026 #212
Country|Currency|Amount|Code|Rate
Australia|dollar|1|AUD|15.134
Brazil|real|1|BRL|3.948
Canada|dollar|1|CAD|15.479
China|renminbi|1|CNY|3.233
Denmark|krone|1|DKK|3.253
Japan|yen|100|JPY|15.812"""

#Class for testing in python
class TestParseRates(unittest.TestCase):
    #test name
    def test_dates(self):
        #define parser results
        dates, rates = parse_rates(SAMPLE)
        #verify if dates really equal the good one
        self.assertEqual(dates,"04 Nov 2026")

    def test_rates(self):
        dates, rates = parse_rates(SAMPLE)
        self.assertEqual(rates["AUD"], (1, 15.134))
        self.assertEqual(rates["JPY"], (100,15.812))

    def test_czk_add(self):
        dates, rates = parse_rates(SAMPLE)
        self.assertEqual(rates["CZK"], (1,1.0))

    def test_newline(self):
        dates, rates = parse_rates(SAMPLE + "\n")
        self.assertEqual(rates["JPY"], (100,15.812))

    def test_invalid_line(self):
        bad_text = "04 Nov 2026 #212\nCountry|Currency|Amount|Code|Rate\nCanadiens de Montreal"
        #This function says this code needs to return a value error with the bad text
        with self.assertRaises(ValueError):
            parse_rates(bad_text)

    def test_short_line(self):
        with self.assertRaises(ValueError):
            parse_rates("")











