from flask import Flask, jsonify, Response, render_template, request
import numpy as np
import pandas as pd
from utils import func
import pickle

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def prediction():
    data = request.form
    if request.method == 'POST':

        Weather = data['Weather']
        Traffic = data['Traffic']
        Vehicle_condition = eval(data['Vehicle_condition'])
        Type_of_order = data['Type_of_order']
        Vehicle = data['Vehicle']
        multiple_deliveries = eval(data['multiple_deliveries'])
        City = data['City']
        Month = eval(data['Month'])
        Day = eval(data['Day'])
        distance_KM = eval(data['distance_KM'])
        Orderd_hour = eval(data['Orderd_hour'])
        Orderd_minute = eval(data['Orderd_minute'])
        Order_picked_minute = eval(data['Order_picked_minute'])
        Age = eval(data['Age'])
        Ratings = eval(data['Ratings'])
    

        result = func(Weather, Traffic, Vehicle_condition, Type_of_order, Vehicle, multiple_deliveries, City, Month,
                      Day, distance_KM, Orderd_hour, Orderd_minute, Order_picked_minute, Age, Ratings)
    
    return render_template('after.html',prediction=result)

if __name__=="__main__":
    app.run(debug=True)