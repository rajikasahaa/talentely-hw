def length_converter(value, from_unit, to_unit):
    # Conversion rates from meters
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    }
    
    # Converting the value to meters first
    value_in_meters = value / length_units[from_unit]
    # Converting from meters to the target unit
    return value_in_meters * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    # Conversion rates from kilograms
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    
    # Converting the value to kilograms first
    value_in_kilograms = value / weight_units[from_unit]
    # Converting from kilograms to the target unit
    return value_in_kilograms * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value     # If from_unit and to_unit are the same

def main():
    print("Unit Converter")
    while True:
        print("\nSelect the type of conversion:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            value = float(input("Enter the length value to convert: "))
            from_unit = input("Enter the current unit (meters, kilometers, centimeters, millimeters, inches, feet, yards, miles): ").lower()
            to_unit = input("Enter the target unit (meters, kilometers, centimeters, millimeters, inches, feet, yards, miles): ").lower()
            converted_value = length_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
        
        elif choice == "2":
            value = float(input("Enter the weight value to convert: "))
            from_unit = input("Enter the current unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
            to_unit = input("Enter the target unit (kilograms, grams, milligrams, pounds, ounces): ").lower()
            converted_value = weight_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
        
        elif choice == "3":
            value = float(input("Enter the temperature value to convert: "))
            from_unit = input("Enter the current unit (celsius, fahrenheit, kelvin): ").lower()
            to_unit = input("Enter the target unit (celsius, fahrenheit, kelvin): ").lower()
            converted_value = temperature_converter(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
        
        elif choice == "4":
            print("Exiting the Unit Converter.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

    

