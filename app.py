import streamlit as st
import time

# Set Page Configuration
st.set_page_config(page_title="Premium Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for Improved Styling & Animation
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f4f9;
        }
        
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(-10px);}
            to {opacity: 1; transform: translateY(0);}
        }
        
        h1, h2 {
            animation: fadeIn 1s ease-in-out;
            color: #4A90E2;
            text-align: center;
        }
        
        .stButton>button {
            background: linear-gradient(135deg, #4CAF50, #8BC34A);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            transition: 0.3s;
            padding: 10px;
        }
        
        .stButton>button:hover {
            background: linear-gradient(135deg, #388E3C, #689F38);
            transform: scale(1.08);
        }
        
        .stSelectbox, .stNumberInput, .stRadio {
            animation: fadeIn 1.2s ease-in-out;
        }
        
        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.05);}
            100% {transform: scale(1);}
        }
        .footer-text {
            text-align: center;
            color: gray;
            font-size: 14px;
            animation: pulse 2s infinite;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <h1>🔄 Premium Unit Converter</h1>
""", unsafe_allow_html=True)

# Sidebar for Conversion Type
unit_type = st.sidebar.radio("Choose Conversion Type:", [
    "📏 Length Converter",
    "⚖️ Weight Converter",
    "🌡️ Temperature Converter",
    "💧 Liquid Converter",
    "⏳ Time Converter",
    "📐 Area Converter"
])

# Conversion Dictionaries
unit_conversions = {
    "📏 Length Converter": {"Kilometre": 1000, "Metre": 1, "Centimetre": 0.01, "Millimetre": 0.001},
    "⚖️ Weight Converter": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
    "💧 Liquid Converter": {"Litre": 1, "Millilitre": 0.001, "Gallon": 3.78541, "Pint": 0.473176},
    "⏳ Time Converter": {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400},
    "📐 Area Converter": {"Square Metre": 1, "Square Kilometre": 1e6, "Hectare": 10000, "Acre": 4046.86}
}

def convert_units(amount, from_unit, to_unit, unit_dict):
    return amount * (unit_dict[to_unit] / unit_dict[from_unit])

if unit_type in unit_conversions:
    st.markdown(f"<h2>{unit_type}</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", list(unit_conversions[unit_type].keys()))
    to_unit = st.selectbox("To:", list(unit_conversions[unit_type].keys()))
    
    if st.button("Convert"):
        with st.spinner("Processing..."):
            time.sleep(1)
        result = convert_units(amount, from_unit, to_unit, unit_conversions[unit_type])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "🌡️ Temperature Converter":
    st.markdown("<h2>🌡️ Temperature Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter Temperature:", format="%.2f")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        with st.spinner("Converting..."):
            time.sleep(1)
        if from_unit == to_unit:
            result = amount
        elif from_unit == "Celsius":
            result = (amount * 9/5 + 32) if to_unit == "Fahrenheit" else (amount + 273.15)
        elif from_unit == "Fahrenheit":
            result = ((amount - 32) * 5/9) if to_unit == "Celsius" else ((amount - 32) * 5/9 + 273.15)
        elif from_unit == "Kelvin":
            result = (amount - 273.15) if to_unit == "Celsius" else ((amount - 273.15) * 9/5 + 32)
        st.success(f"{amount} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("""
    <hr>
    <p class='footer-text'>© 2025 Premium Unit Converter | Developed with ❤️ by Fareed Nathani</p>
""", unsafe_allow_html=True)
