from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained pipeline
model = joblib.load("heart_disease_pipeline.pkl")

# Final threshold chosen in Day 2
THRESHOLD = 0.4

@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON input
    data = request.json

    # Convert JSON to DataFrame (IMPORTANT for ColumnTransformer)
    input_data = pd.DataFrame([data])

    # Predict probability
    prob = model.predict_proba(input_data)[0][1]

    # Apply threshold
    prediction = int(prob >= THRESHOLD)

    # Return result
    return jsonify({
        "probability": float(prob),
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
