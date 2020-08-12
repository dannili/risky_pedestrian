import numpy as np
import joblib
import datetime
from flask import Flask, request, render_template

app = Flask("risky_walker_api")
accident_rf = joblib.load("my_trained_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict_accident():

    user_inputs = [x for x in request.form.values()]
    date_entry = user_inputs[0]
    non_date_entry = user_inputs[1:]
    features_list = []

    year, month, day, hour = map(int, date_entry.split('-'))
    d = datetime.datetime(year, month, day, hour)
    day_of_week = d.weekday()
    day_of_year = d.toordinal() - datetime.datetime(d.year, 1, 1).toordinal() + 1

    for i in (day_of_week, day_of_year, month, hour):
    	features_list.append(i)
    features_list.extend(list(map(int, non_date_entry)))
    features = [np.array(features_list)]
    
    prediction = accident_rf.predict(features)

    if prediction[0] == 0:
        output = f'You are safe!  ({d.strftime("%A")}, {d} | Neighbourhood {user_inputs[1]})'
    else: output = f'Be careful, there could be a pedestrian accident.  ({d.strftime("%A")}, {d} | Neighbourhood {user_inputs[1]})'
    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    
    app.run()
