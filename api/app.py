import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/predict', methods=['post'])
def predict():
    features = [int(x) for x in request.form.values()]
    model_features = [np.array(features)]
    prediction = model.predict(model_features)

    predict_rating = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your rating is : {}'.format(predict_rating))


if __name__ == "__main__":
    app.run(debug=True)