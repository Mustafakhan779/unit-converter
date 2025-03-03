def convert_unit (value:float, from_unit:str, to_unit :str)->float:
    conversion_factor = {
    "length":{
        ("meter","kilometer"):0.001,
        ("kilometer","meter"):1000,
        ("centimeter", "meter"): 0.01,
        ("meter", "centimeter"): 100,
        ("inch", "centimeter"): 2.54,
        ("centimeter", "inch"): 1 / 2.54,
        ("meter", "inch"): 39.3701,    
        ("inch", "meter"): 1 / 39.3701
    },
    "temperature":{
        ("celsius", "fahrenheit"):lambda c : (c * 9/5) + 32,
        ("fahrenheit", "celsius"):lambda f : (f - 32) * 5/9
    },
    "weight":{
        ("gram","kilogram"):0.001,
        ("kilogram","gram"):1000,
        ("pound", "kilogram"): 0.453592,
        ("kilogram", "pound"): 1 / 0.453592
    }
 }


  


    for category,conversions in conversion_factor.items():

        if (from_unit, to_unit) in conversions:
            conversions = conversions[from_unit, to_unit]
            return conversions(value) if callable(conversions) else value * conversions
    print("❌ Conversion not supported.")
    return None



def main():
    categories = {
        "1":"length",
        "2":"temperature",
        "3":"weight"
    }
    units = {
        "length":["meter", "kilometer","centimeter", "inch"],
        "temperature" : ["celsius", "fahrenheit"],
        "weight" : ["gram", "kilogram", "pound"]
    }

    print("\n📏 Welcome to the Unit Converter! 🚀")
    print("Select a category:")


    
    for key, category in categories.items():
        print(f"{key}.{category}")
    category_choice = input("Enter your choice (1/2/3): ").strip()
    category = categories.get(category_choice)

    if not category :
        print("❌ Invalid category choice. Exiting...")
        return
    print(f"\n📌 You selected: {category}")
    print("Available units:", ", ".join(units[category]))


    from_unit = input("\n convert from: ").strip().lower()
    to_unit = input("\n convert to: ").strip().lower()

    if from_unit not in units[category] or to_unit not in units[category]:
        print("❌ Invalid unit selection.")
        return
    try:
        value = float(input("Enter Value: "))
        result = convert_unit(value , from_unit, to_unit)
        if result is not None:
            print(f"✅ Converted Value: {result} {to_unit}")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")


if __name__ == "_main_":
    main()