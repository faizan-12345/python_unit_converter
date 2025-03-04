import streamlit as st
import pandas as pd

# Set up Streamlit App
st.set_page_config(page_title="📏 Unit Converter Pro", layout="wide", page_icon="📏")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stTextInput input {
        font-size: 16px;
    }
    .stSelectbox select {
        font-size: 16px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
    }
    .stMarkdown h2 {
        color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Menu
st.sidebar.title("📏 Unit Converter Pro")
menu = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🌡️ Temperature", "📏 Length", "⚖️ Weight", "💧 Volume", "📅 History"]
)

# Home Page
if menu == "🏠 Home":
    st.title("Welcome to Unit Converter Pro! 🎉")
    st.markdown("""
    ### **How to Use the App**
    1. Select the type of unit conversion from the sidebar menu.
    2. Enter the value you want to convert.
    3. Select the input unit and the target unit.
    4. Click **Convert** to see the result.

    ### **Benefits**
    - **Dynamic Conversions**: Accurate and flexible conversions.
    - **User-Friendly**: Simple and intuitive interface.
    - **Multiple Units**: Convert temperature, length, weight, volume, and more!
    """)

# Custom Conversion Functions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    return value

def convert_length(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        "Liters": 1,
        "Milliliters": 1000,
        "Gallons": 0.264172,
        "Cubic Meters": 0.001
    }
    return value * conversions[to_unit] / conversions[from_unit]

# Save Conversion to History
def save_to_history(input_value, input_unit, target_unit, result):
    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append([input_value, input_unit, target_unit, result])

# Temperature Conversion Page
if menu == "🌡️ Temperature":
    st.title("🌡️ Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        input_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        target_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(input_value, input_unit, target_unit)
        st.success(f"**Result:** {input_value} {input_unit} = {result:.2f} {target_unit}")
        save_to_history(input_value, input_unit, target_unit, result)  # Save to history

# Length Conversion Page
if menu == "📏 Length":
    st.title("📏 Length Converter")
    col1, col2 = st.columns(2)
    with col1:
        input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        input_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
    with col2:
        target_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
    if st.button("Convert"):
        result = convert_length(input_value, input_unit, target_unit)
        st.success(f"**Result:** {input_value} {input_unit} = {result:.2f} {target_unit}")
        save_to_history(input_value, input_unit, target_unit, result)  # Save to history

# Weight Conversion Page
if menu == "⚖️ Weight":
    st.title("⚖️ Weight Converter")
    col1, col2 = st.columns(2)
    with col1:
        input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        input_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    with col2:
        target_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert"):
        result = convert_weight(input_value, input_unit, target_unit)
        st.success(f"**Result:** {input_value} {input_unit} = {result:.2f} {target_unit}")
        save_to_history(input_value, input_unit, target_unit, result)  # Save to history

# Volume Conversion Page
if menu == "💧 Volume":
    st.title("💧 Volume Converter")
    col1, col2 = st.columns(2)
    with col1:
        input_value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        input_unit = st.selectbox("From", ["Liters", "Milliliters", "Gallons", "Cubic Meters"])
    with col2:
        target_unit = st.selectbox("To", ["Liters", "Milliliters", "Gallons", "Cubic Meters"])
    if st.button("Convert"):
        result = convert_volume(input_value, input_unit, target_unit)
        st.success(f"**Result:** {input_value} {input_unit} = {result:.2f} {target_unit}")
        save_to_history(input_value, input_unit, target_unit, result)  # Save to history

# History Page
if menu == "📅 History":
    st.title("📅 Conversion History")
    if "history" not in st.session_state:
        st.session_state.history = []
    if st.session_state.history:
        history_df = pd.DataFrame(st.session_state.history, columns=["Input Value", "Input Unit", "Target Unit", "Result"])
        st.dataframe(history_df)
    else:
        st.write("No conversion history yet.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Muhammad Faizan")