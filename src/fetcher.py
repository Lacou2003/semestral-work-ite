"""Download the daily exchange rates from the Czech National Bank (CNB)."""

import requests

URL = "https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt"


def fetch_rates_text():
    """Download today's CNB exchange rates as plain text.

    Returns:
        str: Raw text of the CNB daily rates file.

    Raises:
        ConnectionError: If the CNB website cannot be reached.
    """
    try:
        # download the page (give up after 10 seconds)
        response = requests.get(URL, timeout=10)
        # raise an error if the server answers with an error code
        response.raise_for_status()
    except requests.RequestException:
        raise ConnectionError("Could not reach the CNB. Check your internet connection.")

    # return the content as text
    return response.text

if __name__ == "__main__":
    print(fetch_rates_text())