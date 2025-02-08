from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
from app import find_nearest_cat, scaler  # Import function and scaler from app.py

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    #display html file
    return send_from_directory('','www/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json
        age = float(data.get("age"))
        weight = float(data.get("weight"))
        activity_level = data.get("activity_level").lower()
        print("hi", age, weight, activity_level)
        # Validate activity level
        if activity_level not in ['high', 'low', 'moderate']:
            return jsonify({"error": "Invalid activity level! Must be 'high', 'low', or 'moderate'."}), 400
        
        # Convert activity level to numeric
        activity_level_encoded = 0 if activity_level == 'low' else 1 if activity_level == 'moderate' else 2
        
        # Prepare input for model
        user_input = np.array([[age, weight, activity_level_encoded]])
        
        # Call the prediction function
        result = find_nearest_cat(user_input)
        
        return result, 200  # Return the JSON result

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
