import joblib
import numpy as np
import os

file_path = os.path.join(os.path.dirname("/home/ek/Documents/10Xtutor/ML_Journey/ML001-Project-Sources-Code-and-Learning-Materials/Notebooks Used in the course/Stock Price Predictor/"), "rigidmodel.pkl")

def preprocess(Open, High, Low, Volume):
    # Convert input values to numeric types
    Open = float(Open)
    High = float(High)
    Low = float(Low)
    Volume = float(Volume)

    test_data = np.array([[Open, High, Low, Volume]])
    trained_model = joblib.load(file_path)
    prediction = trained_model.predict(test_data)
    print(prediction)
    return prediction