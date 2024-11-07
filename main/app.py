#Deployment 
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('../model/best_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract features
    ability = data['ability']
    difficulty = data['difficulty']
    year = data['year']
    
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'ability': [ability],
        'difficulty': [difficulty],
        'year': [year]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as JSON
    result = {
        'prediction': int(prediction[0])  # Convert numpy int to regular int
    }
    
    return jsonify(result)

# Define a test route
@app.route('/health', methods=['GET'])
def health():
    return "Model is up and running!"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
