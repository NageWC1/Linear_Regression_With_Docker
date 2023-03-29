import pickle
import json
# import the libraries from flask that we going to use here 
from flask import Flask,request,app,jsonify,url_for,render_template
# we will import some of the main libraries that we going to use here 
import numpy as np 
import pandas as pd


# define the flask app
app = Flask(__name__)
# load our model
regmodel = pickle.load(open("regmodel.pkl","rb"))
scaler =pickle.load(open("scalling.pkl","rb"))

@app.route('/')
def home():
    return render_template('home.html')

# we here creating a api to run the model, get the prediction and retur the predicted value 
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # just check about github copilot that helps to auto generate the code when we start the code 
    data = request.json['data']
    print(data)
    # the data will be in sinle dimention, but we have to take it as 2 dimension
    # that done by below code 
    print(np.array(list(data.values())).reshape(1,-1))
    # and we stadadize the value before passing to the predict, otherwise the calculation will be wrong
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    # the out will get the data as 2 dimentional array so we getting the value which stored 0th element
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    # after the predcition form the flask application we going to render the html page with a place holder
    # the place holder will replcaed with passing place holder
    return render_template('home.html',prediction_text="The House price prediction is {}".format(output))

if __name__== '__main__':
    app.run(debug=True)