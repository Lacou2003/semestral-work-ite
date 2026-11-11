"""With this link : https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/daily.txt
The program will receive these information :
04 Nov 2026 #212
Country|Currency|Amount|Code|Rate
Australia|dollar|1|AUD|15.134
Brazil|real|1|BRL|3.948
Canada|dollar|1|CAD|15.479
China|renminbi|1|CNY|3.233
Denmark|krone|1|DKK|3.253
...
The goal of the parser is to transform this information into this 2 sections :
 1. The date "04 nov 2026"
 2. A currency dictionairy
    "CZK": (1, 1.0),
    "EUR": (1, 24.335),
    "JPY": (100, 15.812),
    "USD": (1, 22.101)
"""
#main function
def parse_rates(text) :
    #divide in lines and remove spaces
    lines = text.strip().split("\n")
    #if the line is not on the good format we return an error
    if len(lines) < 3:
        raise ValueError("Invalid CNB data : Not enought lines")
    #first line is always the date, we remove the # and the spaces
    first_line = lines[0]
    date = first_line.split("#")[0]
    date = date.strip()
    #this is the format we want
    rates = {"CZK": (1, 1.0)}
    for line in lines[2:]:
        #we splits the lines at the |
        parts = line.split("|")
        #if its not the good format = error
        if len(parts) != 5 :
            raise ValueError("CNB invalid line :" +line)
        #we divide the information
        unit = int(parts[2])
        code = parts[3]
        rate = float(parts[4])
        rates[code] = (unit, rate)

    return date, rates
