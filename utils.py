import pickle
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('random_forest.pickle','rb'))

project_data = {"Weather":{"Cloudy":0,"Fog":1,"Sandstorms":2,"Stormy":3,"Sunny":4,"Windy":5},
                "Traffic":{"High":0,"Jam":1,"Low":2,"Medium":3},
                "Type_of_order":{"Buffet":0,"Drinks":1,"Meal":2,"Snack":3},
                "Vehicle":{"bicycle":0,"electric_scooter":1,"motorcycle":2,"scooter":3},
                "City":{"Metropolitian":0,"Semi-Urban":1,"Urban":2}}

def func(Weather, Traffic, Vehicle_condition, Type_of_order, Vehicle, multiple_deliveries, City, Month, Day,
         distance_KM, Orderd_hour, Orderd_minute, Order_picked_minute, Age, Ratings):
    
    test = np.zeros(15)
    test[0] = project_data['Weather'][Weather]
    test[1] = project_data['Traffic'][Traffic] 
    test[2] = Vehicle_condition
    test[3] = project_data['Type_of_order'][Type_of_order]
    test[4] = project_data['Vehicle'][Vehicle]
    test[5] = multiple_deliveries
    test[6] = project_data['City'][City]
    test[7] = Month
    test[8] = Day
    test[9] = distance_KM
    test[10] = Orderd_hour
    test[11] = Orderd_minute
    test[12] = Order_picked_minute
    test[13] = Age
    test[14] = Ratings

    data = pd.DataFrame(data=[test])
    
    result = model.predict(data.values)
    
    return result
