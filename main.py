import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #0000FF; /* Change this to your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.header("Welcome to Ultimate Unit converter!")

option = st.selectbox(
    "Which unit would you like to convert?",
    ("📏Length", "🌡️Temperature", "⚖️Weight", "🫙Volume", "📦Area", "🚄Speed", "⌚Time", "⛽Pressure",),
)

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "millimeters": 0.001,
        "centimeters": 0.01,
        "meters": 1,
        "kilometers": 1000,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

if option == "📏Length":
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
    value = st.number_input("Enter value", 0.0)
    result = convert_length(value, from_unit, to_unit)
    st.write(f"### Result: {result} {to_unit}")




if option == "🌡️Temperature":
    st.subheader("Temperature Converter")
    from_unit = st.selectbox("From unit", ("Celsius", "Fahrenheit", "Kelvin"))
    to_unit = st.selectbox("To unit", ("Celsius", "Fahrenheit", "Kelvin"))
    value = st.number_input("Enter value", 0.0)
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9 / 5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5 / 9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9 / 5 + 32
    else:
        result = value
    st.write(f"### Result: {result} {to_unit}")
