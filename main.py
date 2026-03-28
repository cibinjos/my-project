# main.py — Interactive CLI for the unit converter

import converter

# ── Menu definitions ───────────────────────────────────────────────────────

CATEGORIES = {
    "1": "Temperature",
    "2": "Weight",
    "3": "Length",
    "4": "Speed",
}

CONVERSIONS = {
    "1": [
        ("Fahrenheit → Celsius",  converter.fahrenheit_to_celsius,  "°F", "°C"),
        ("Celsius → Fahrenheit",  converter.celsius_to_fahrenheit,  "°C", "°F"),
        ("Fahrenheit → Kelvin",   converter.fahrenheit_to_kelvin,   "°F", "K"),
        ("Kelvin → Fahrenheit",   converter.kelvin_to_fahrenheit,   "K",  "°F"),
        ("Celsius → Kelvin",      converter.celsius_to_kelvin,      "°C", "K"),
        ("Kelvin → Celsius",      converter.kelvin_to_celsius,      "K",  "°C"),
    ],
    "2": [
        ("Kilograms → Pounds",    converter.kg_to_lb,               "kg", "lb"),
        ("Pounds → Kilograms",    converter.lb_to_kg,               "lb", "kg"),
    ],
    "3": [
        ("Centimeters → Feet",    converter.cm_to_feet,             "cm", "ft"),
        ("Feet → Centimeters",    converter.feet_to_cm,             "ft", "cm"),
        ("Meters → Yards",        converter.meters_to_yards,        "m",  "yd"),
        ("Yards → Meters",        converter.yards_to_meters,        "yd", "m"),
    ],
    "4": [
        ("km/h → mph",            converter.kmh_to_mph,             "km/h", "mph"),
        ("mph → km/h",            converter.mph_to_kmh,             "mph",  "km/h"),
    ],
}


# ── Helpers ────────────────────────────────────────────────────────────────

def print_main_menu():
    print("\n=== Unit Converter ===")
    for key, name in CATEGORIES.items():
        print(f"  {key}. {name}")
    print("  0. Quit")


def print_sub_menu(cat_key):
    cat_name = CATEGORIES[cat_key]
    print(f"\n--- {cat_name} ---")
    for i, (label, _, from_unit, to_unit) in enumerate(CONVERSIONS[cat_key], start=1):
        print(f"  {i}. {label}")


def get_category_choice():
    while True:
        print_main_menu()
        choice = input("\nSelect category: ").strip()
        if choice == "0":
            return None
        if choice in CATEGORIES:
            return choice
        print(f"  Invalid choice '{choice}'. Please enter 1–{len(CATEGORIES)} or 0 to quit.")


def get_conversion_choice(cat_key):
    options = CONVERSIONS[cat_key]
    while True:
        print_sub_menu(cat_key)
        choice = input("\nSelect conversion: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"  Invalid choice '{choice}'. Please enter 1–{len(options)} or 0 to go back.")


def get_numeric_input(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Please try again.")


# ── Main loop ──────────────────────────────────────────────────────────────

def main():
    print("Welcome to the Unit Converter!")
    while True:
        cat_key = get_category_choice()
        if cat_key is None:
            print("Goodbye!")
            break

        conversion = get_conversion_choice(cat_key)
        if conversion is None:
            continue

        label, fn, from_unit, to_unit = conversion
        value = get_numeric_input(f"Enter value in {from_unit}: ")

        try:
            result = fn(value)
            print(f"\n  Result: {value} {from_unit} = {round(result, 4)} {to_unit}")
        except ValueError as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()
