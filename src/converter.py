"""Convert an amount between two currencies using CNB rates."""

def convert(amount, from_code, to_code, rates):
    #gader rates and informations
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





