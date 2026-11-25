import sys
from src.parser import parse_rates
from src.converter import convert
from src.fetcher import fetch_rates_text

def main():
    amount = float(sys.argv[1])
    from_code = (sys.argv[2]).upper()
    to_code = (sys.argv[3]).upper()
    text = fetch_rates_text()
    dates, rates = parse_rates(text)
    result = convert(amount, from_code, to_code, rates)
    print(f"{amount:.2f} {from_code} = {result:.2f} {to_code} (CNB rates from {dates})")

if __name__ == "__main__":
    main()