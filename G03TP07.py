from forex_python.converter import CurrencyRates, CurrencyCodes

def currency_converter(amount, currency1, currency2):
    c = CurrencyRates()
    try:
        converted_amount = c.convert(currency1, currency2, amount)
        return converted_amount
    except Exception as e:
        return str(e)

def main():
    print("CURRENCY CONVERTOR")

    try:
        amount = float(input("Enter the amount you want to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # INPUTS
    currency1 = input("Enter the currency code you want to convert from (e.g., USD, EUR): ").upper()
    currency2 = input("Enter the currency code you want to convert to: ").upper()
    #CONVERSION
    converted_amount = currency_converter(amount, currency1, currency2)


    currency_symbol = CurrencyCodes().get_symbol(currency2)

    #DISPLAY
    print(f"{amount} {currency1} is equal to {currency_symbol}{converted_amount:.2f} {currency2}")

if __name__ == "__main__":
    main()