"""Command-line entry point of the CNB currency converter.

Usage:
    python main.py <amount> <from> <to>

Example:
    python main.py 100 EUR USD
"""

import sys

from src.converter import convert
from src.fetcher import fetch_rates_text
from src.parser import parse_rates


def main():
    """Read the arguments, convert the amount and print the result."""
    # 1. check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <amount> <from> <to>")
        print("Example: python main.py 100 EUR USD")
        sys.exit(1)

    # 2. read the amount
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print(f"Error: invalid amount '{sys.argv[1]}'")
        sys.exit(1)

    from_code = sys.argv[2].upper()
    to_code = sys.argv[3].upper()

    # 3. download, parse and convert
    try:
        text = fetch_rates_text()
        date, rates = parse_rates(text)
        result = convert(amount, from_code, to_code, rates)
    except ConnectionError as error:
        print(f"Error: {error}")
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

    # 4. print the result
    print(f"{amount:.2f} {from_code} = {result:.2f} {to_code} (CNB rates from {date})")


if __name__ == "__main__":
    main()