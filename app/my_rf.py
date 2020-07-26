import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask("risky_walker_api")
accident_rf = joblib.load("my_trained_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict_accident():
    input_json = request.get_json(force=True)
    print(f'Data sent in request:{input_json}')

    # Read the input data
    input_data_df = pd.DataFrame.from_dict(input_json, orient='columns')

    # Process in the model and make predictions
    is_accident = accident_rf.predict(input_data_df)

    preiction = is_accident.tolist()
    return jsonify(preiction)

if __name__ == "__main__":
    
    app.run()
