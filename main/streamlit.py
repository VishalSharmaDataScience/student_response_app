import streamlit as st
import requests
import json

# Streamlit app title
st.title("Student Question Answer Prediction")

# User inputs for the model
ability = st.number_input("Enter student's ability level:", format="%.2f")
difficulty = st.number_input("Enter question difficulty level:", format="%.2f")
year = st.selectbox("Select year:", [2021, 2022])

# Button to make prediction
if st.button("Predict"):
    # Define the data to be sent in the POST request
    input_data = {
        "ability": ability,
        "difficulty": difficulty,
        "year": year
    }
    
    # Send POST request to the Flask API
    try:
        response = requests.post("http://192.168.0.103:8080/predict", 
                                 data=json.dumps(input_data), 
                                 headers={"Content-Type": "application/json"})
        # Handle the response
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            result_text = "Correct" if prediction == 1 else "Incorrect"
            st.success(f"The model predicts the student will answer: {result_text}")
        else:
            st.error("Error in prediction request. Please check the server.")
    except requests.exceptions.RequestException as e:
        st.error("Error: Could not connect to the prediction server.")
        st.write(e)
