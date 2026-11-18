"""Convert an amount between two currencies using CNB rates."""

def convert(amount, from_code, to_code, rates):
    """Convert an amount from one currency to another via CZK.

        Args:
            amount (float): Amount of money to convert. Must be greater than 0.
            from_code (str): Code of the source currency (e.g. "EUR").
            to_code (str): Code of the target currency (e.g. "USD").
            rates (dict): Rates from the parser, as {code: (unit, rate)}.

        Returns:
            float: Converted amount rounded to 2 decimals.

        Raises:
            ValueError: If the amount is not positive or a currency is unknown.
        """
    if amount <= 0:
        raise ValueError("Amount should be greater than zero!")
    if from_code not in rates:
        raise ValueError("Unknown currency: " + from_code)
    if to_code not in rates:
        raise ValueError("Unknown currency: " + to_code)

    #gather rates and informations
    unit_from, rate_from = rates[from_code]
    unit_to, rate_to = rates[to_code]
    #basic calculations
    czk = amount*rate_from/unit_from
    result = czk*unit_to/rate_to
    #keep 2 decimals
    final_amount = round(result, 2)
    return final_amount

if __name__ == "__main__":
    rates = {"CZK": (1, 1.0), "EUR": (1, 24.335), "JPY": (100, 15.812)}
    print(convert(5000, "JPY", "CZK", rates))





