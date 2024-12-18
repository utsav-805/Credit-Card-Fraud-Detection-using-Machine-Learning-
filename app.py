from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('model.pkl', 'rb'))

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # Replace with your HTML file for the frontend

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input data
        data = request.json
        
        # Extract features: Time, V1-V28, and Amount
        features = [
            data['Time'], data['V1'], data['V2'], data['V3'], data['V4'], data['V5'], data['V6'], 
            data['V7'], data['V8'], data['V9'], data['V10'], data['V11'], data['V12'], data['V13'], 
            data['V14'], data['V15'], data['V16'], data['V17'], data['V18'], data['V19'], data['V20'], 
            data['V21'], data['V22'], data['V23'], data['V24'], data['V25'], data['V26'], data['V27'], 
            data['V28'], data['Amount']
        ]

        # Convert features into a DataFrame
        input_data = pd.DataFrame([features], columns=[
            'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 
            'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 
            'V27', 'V28', 'Amount'
        ])

        # Predict class (Fraudulent or Legitimate)
        prediction = model.predict(input_data)
        result = 'Fraudulent' if prediction[0] == 1 else 'Legitimate'

        # Return the prediction as JSON
        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
