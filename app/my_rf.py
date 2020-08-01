import numpy as np
import joblib
from flask import Flask, request, render_template

app = Flask("risky_walker_api")
accident_rf = joblib.load("my_trained_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict_accident():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = accident_rf.predict(final_features)

    if prediction[0] == 0:
        output = 'Yes, you are safe.'
    else: output = 'No, there could be a pedestrian accident.'

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    
    app.run()
