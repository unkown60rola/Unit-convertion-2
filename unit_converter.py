import streamlit as st

def convert_unit(value, from_unit, to_unit):
    conversions = {
        "millimeters_centimeters": 0.1,
        "centimeters_millimeters": 10,
        "millimeters_meters": 0.001,
        "meters_millimeters": 1000,
        "millimeters_kilometers": 0.000001,
        "kilometers_millimeters": 1_000_000,
        "millimeters_inches": 0.0393701,
        "inches_millimeters": 25.4,
        "millimeters_feet": 0.00328084,
        "feet_millimeters": 304.8,
        "millimeters_yards": 0.00109361,
        "yards_millimeters": 914.4,
        "millimeters_miles": 0.000000621371,
        "miles_millimeters": 1_609_344,
        "centimeters_meters": 0.01,
        "meters_centimeters": 100,
        "centimeters_kilometers": 0.00001,
        "kilometers_centimeters": 100_000,
        "centimeters_inches": 0.393701,
        "inches_centimeters": 2.54,
        "centimeters_feet": 0.0328084,
        "feet_centimeters": 30.48,
        "centimeters_yards": 0.0109361,
        "yards_centimeters": 91.44,
        "centimeters_miles": 0.00000621371,
        "miles_centimeters": 160_934,
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "meters_inches": 39.3701,
        "inches_meters": 0.0254,
        "meters_feet": 3.28084,
        "feet_meters": 0.3048,
        "meters_yards": 1.09361,
        "yards_meters": 0.9144,
        "meters_miles": 0.000621371,
        "miles_meters": 1609.34,
        "kilometers_inches": 39_370.1,
        "inches_kilometers": 0.0000254,
        "kilometers_feet": 3_280.84,
        "feet_kilometers": 0.0003048,
        "kilometers_yards": 1_093.61,
        "yards_kilometers": 0.0009144,
        "kilometers_miles": 0.621371,
        "miles_kilometers": 1.60934,
        "inches_feet": 0.0833333,
        "feet_inches": 12,
        "inches_yards": 0.0277778,
        "yards_inches": 36,
        "inches_miles": 0.0000157828,
        "miles_inches": 63_360,
        "feet_yards": 0.333333,
        "yards_feet": 3,
        "feet_miles": 0.000189394,
        "miles_feet": 5280,
        "yards_miles": 0.000568182,
        "miles_yards": 1760,
    }
    
    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        return value * conversions[key]
    else:
        return value
    
st.header("Welcome to Ultimate Unit converter!")
    
Units = st.selectbox(
        "Which unit would you like to convert?",
        ("📏Length", "🌡️Temperature", "⚖️Weight",),
    )
value = st.number_input("Enter value", 0.0)
    
if Units == "📏Length":
        st.subheader("Length Converter")
        from_unit = st.selectbox(
            "From unit",
            (
                "millimeters",
                "centimeters",
                "meters",
                "kilometers",
                "inches",
                "feet",
                "yards",
                "miles",
            ),
        )
        to_unit = st.selectbox(
            "To unit",
            (
                "millimeters",
                "centimeters",
                "meters",
                "kilometers",
                "inches",
                "feet",
                "yards",
                "miles",
            ),
        )
        if st.button("Convert"):
            result = convert_unit(value, from_unit, to_unit)  
            st.write(f"Converted Value: {result}")


def convert_temperature(value, from_unit, to_unit):
    conversions = {
        "Celsius_Fahrenheit": lambda c: (c * 9 / 5) + 32,
        "Fahrenheit_Celsius": lambda f: (f - 32) * 5 / 9,
        "Celsius_Kelvin": lambda c: c + 273.15,
        "Kelvin_Celsius": lambda k: k - 273.15,
        "Fahrenheit_Kelvin": lambda f: (f - 32) * 5 / 9 + 273.15,
        "Kelvin_Fahrenheit": lambda k: (k - 273.15) * 9 / 5 + 32,
        "Celsius_Rankine": lambda c: (c + 273.15) * 9 / 5,
        "Rankine_Celsius": lambda r: (r - 491.67) * 5 / 9,
        "Fahrenheit_Rankine": lambda f: f + 459.67,
        "Rankine_Fahrenheit": lambda r: r - 459.67,
        "Kelvin_Rankine": lambda k: k * 9 / 5,
        "Rankine_Kelvin": lambda r: r * 5 / 9,
        "Celsius_Delisle": lambda c: (100 - c) * 3 / 2,
        "Delisle_Celsius": lambda d: 100 - (d * 2 / 3),
        "Kelvin_Delisle": lambda k: (373.15 - k) * 3 / 2,
        "Delisle_Kelvin": lambda d: 373.15 - (d * 2 / 3),
        "Fahrenheit_Delisle": lambda f: (212 - f) * 5 / 6,
        "Delisle_Fahrenheit": lambda d: 212 - (d * 6 / 5),
        "Rankine_Delisle": lambda r: (671.67 - r) * 5 / 6,
        "Delisle_Rankine": lambda d: 671.67 - (d * 6 / 5),
        "Celsius_Newton": lambda c: c * 0.33,
        "Newton_Celsius": lambda n: n / 0.33,
        "Celsius_Reaumur": lambda c: c * 0.8,
        "Reaumur_Celsius": lambda re: re / 0.8,
        "Celsius_Romer": lambda c: (c * 21 / 40) + 7.5,
        "Romer_Celsius": lambda ro: (ro - 7.5) * 40 / 21,
        "Celsius_Planck": lambda c: (c + 273.15) / 1.416784e32,
        "Planck_Celsius": lambda p: (p * 1.416784e32) - 273.15,
    }

    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        return conversions[key](value)
    else:
        return value  
        
if Units == "🌡️Temperature":
    st.subheader("Temperature Converter")
    from_unit = st.selectbox(
        "From unit",
        (
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Rankine",
            "Delisle",
            "Newton",
            "Reaumur",
            "Romer",
            "Planck",
        ),
    )
    to_unit = st.selectbox(
        "To unit",
        (
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Rankine",
            "Delisle",
            "Newton",
            "Reaumur",
            "Romer",
            "Planck",
        ),
    )
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"Converted Value: {result} {to_unit}")


def convert_weight(value, from_unit, to_unit):
    conversions = {
        "grams_kilograms": lambda g: g / 1000,
        "kilograms_grams": lambda kg: kg * 1000,
        "grams_pounds": lambda g: g * 0.00220462,
        "pounds_grams": lambda lb: lb / 0.00220462,
        "grams_ounces": lambda g: g * 0.035274,
        "ounces_grams": lambda oz: oz / 0.035274,
        "kilograms_pounds": lambda kg: kg * 2.20462,
        "pounds_kilograms": lambda lb: lb / 2.20462,
        "kilograms_ounces": lambda kg: kg * 35.274,
        "ounces_kilograms": lambda oz: oz / 35.274,
        "pounds_ounces": lambda lb: lb * 16,
        "ounces_pounds": lambda oz: oz / 16,
        "kilograms_stones": lambda kg: kg / 6.35029,
        "stones_kilograms": lambda st: st * 6.35029,
        "grams_milligrams": lambda g: g * 1000,
        "milligrams_grams": lambda mg: mg / 1000,
        "kilograms_metric_tons": lambda kg: kg / 1000,
        "metric_tons_kilograms": lambda mt: mt * 1000,
        "pounds_us_tons": lambda lb: lb / 2000,
        "us_tons_pounds": lambda ust: ust * 2000,
    }

    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        return conversions[key](value)
    else:
        return value  

if Units == "⚖️Weight":
    st.subheader("Weight Converter")
    from_unit = st.selectbox(
        "From unit",
        (
            "grams",
            "kilograms",
            "pounds",
            "ounces",
            "stones",
            "milligrams",
            "metric tons",
            "US tons",
        ),
    )
    to_unit = st.selectbox(
        "To unit",
        (
            "grams",
            "kilograms",
            "pounds",
            "ounces",
            "stones",
            "milligrams",
            "metric tons",
            "US tons",
        ),
    )
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"Converted Value: {result} {to_unit}")
