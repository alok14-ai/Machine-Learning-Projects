import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Mobile price prediction.sav")

# Set the title of the Streamlit app
st.title("Mobile Price Prediction")

# Add input fields for user to enter data
st.header("Enter the features of the mobile phone:")
battery_power = st.number_input("Battery Power", min_value=0)
ram = st.number_input("RAM", min_value=0)
px_height = st.number_input("Pixel Height", min_value=0)
px_width = st.number_input("Pixel Width", min_value=0)
mobile_wt = st.number_input("Mobile Weight", min_value=0)

# Predict button
if st.button("Predict"):
    # Prepare the input data as a numpy array
    input_data = np.array([[battery_power, ram, px_height, px_width, mobile_wt]])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.success(f"The predicted price range is: {prediction[0]}")

