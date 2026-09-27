import joblib
import pandas as pd
from flask import Flask, request, jsonify

learn_api = Flask("__ExtraaLearn__")

MODEL_PATH = "backend_files/dtree_tuned.joblib"
model = joblib.load(MODEL_PATH)

@learn_api.get('/')
def home():
    return "Welcome to the Lead Prediction System"

@learn_api.post('/v1/predict')
def predict_sales():
    try:
        data = request.get_json()

        required_fields = [
            'age', 'website_visits', 'time_spent_on_website', 'page_views_per_visit',
            'current_occupation', 'first_interaction', 'profile_completed', 'last_activity', 'print_media_type1',
            'print_media_type2', 'digital_media', 'educational_channels', 'referral'
        ]

        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({
                "error": "Missing required fields",
                "missing_fields": missing_fields
            }), 400

        sample = {field: data[field] for field in required_fields}

        input_data = pd.DataFrame([sample])

        prediction = model.predict(input_data)[0]

        return jsonify({'Lead': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    learn_api.run(debug=True)
