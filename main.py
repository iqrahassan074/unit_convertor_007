import streamlit as st


st.set_page_config(page_title="Unit Converter", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color:rgb(156, 127, 88);
    }
    .stButton>button {
        background-color:rgb(25, 7, 9);
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color:rgb(194, 186, 201);
        border-radius: 10px;
    }
    .stSelectbox>div>div>input {
        background-color:rgb(73, 34, 34);
        border-radius: 10px;
    }
    .stTitle {
        color:rgb(35, 25, 28);
    }
    .stMarkdown {
        color:rgb(89, 56, 67);
    }
    .output {
        font-size: 24px;
        font-weight: bold;
        color:rgb(8, 7, 8);
    }
    </style>
    """, unsafe_allow_html=True
)


st.title(" Stylish Unit Converter ")


st.sidebar.title("Choose Unit Type")
unit_type = st.sidebar.selectbox(
    "Select the unit category", 
    ["Length", "Mass", "Temperature", "Speed"]
)


def length_conversion():
    st.subheader("Length Converter")
    units = ["meters", "kilometers", "miles", "yards", "centimeters"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    
    value = st.number_input("Enter value", min_value=0.0, value=1.0)
    
    conversion_rates = {
        ("meters", "kilometers"): 0.001,
        ("meters", "miles"): 0.000621371,
        ("meters", "yards"): 1.09361,
        ("meters", "centimeters"): 100,
    }
    
   
    if st.button("Convert"):
        result = value * conversion_rates.get((from_unit, to_unit), 1)
        st.markdown(f'<div class="output">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)


def mass_conversion():
    st.subheader("Mass Converter")
    units = ["grams", "kilograms", "pounds", "ounces"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    
    value = st.number_input("Enter value", min_value=0.0, value=1.0)
    
    conversion_rates = {
        ("grams", "kilograms"): 0.001,
        ("grams", "pounds"): 0.00220462,
        ("grams", "ounces"): 0.035274,
    }
    
    
    if st.button("Convert"):
        result = value * conversion_rates.get((from_unit, to_unit), 1)
        st.markdown(f'<div class="output">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)


def temperature_conversion():
    st.subheader("Temperature Converter")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    
    value = st.number_input("Enter value", min_value=-273.15, value=0.0)
    
    
    if st.button("Convert"):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        
        st.markdown(f'<div class="output">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)


def speed_conversion():
    st.subheader("Speed Converter")
    units = ["m/s", "km/h", "mph", "ft/s"]
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    
    value = st.number_input("Enter value", min_value=0.0, value=1.0)
    
    conversion_rates = {
        ("m/s", "km/h"): 3.6,
        ("m/s", "mph"): 2.23694,
        ("m/s", "ft/s"): 3.28084,
    }
    
 
    if st.button("Convert"):
        result = value * conversion_rates.get((from_unit, to_unit), 1)
        st.markdown(f'<div class="output">{value} {from_unit} = {result} {to_unit}</div>', unsafe_allow_html=True)


if unit_type == "Length":
    length_conversion()
elif unit_type == "Mass":
    mass_conversion()
elif unit_type == "Temperature":
    temperature_conversion()
else:
    speed_conversion()
