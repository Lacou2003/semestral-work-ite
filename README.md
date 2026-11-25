# CNB Currency Converter

Command-line tool that converts an amount between two currencies using today's
official exchange rates from the Czech National Bank (CNB).

## Installation

Requires Python 3.8+ and an internet connection.

```
git clone https://github.com/Lacou2003/semestral-work-ite.git
cd semestral-work-ite
python -m pip install -r requirements.txt
```

## Usage

```
python main.py <amount> <from> <to>
```

**Input:** a positive amount and two currency codes (e.g. `EUR`, `USD`, `CZK`).
**Output:** the converted amount (2 decimals) and the date of the rates.

```
$ python main.py 100 EUR USD
100.00 EUR = 109.43 USD (CNB rates from 25 Nov 2026)
```

Invalid input (bad amount, unknown currency, no connection) prints a short error message.

## Tests

```
python test_main.py
```

See [docs/tests.md](docs/tests.md) for the testing approach.

## Limitations

- Needs internet; CNB updates rates once per working day (~14:30).
- Only CNB-listed currencies (~30) and CZK; today's rates only.
- One conversion per command.

## License

MIT, see [LICENSE](LICENSE).