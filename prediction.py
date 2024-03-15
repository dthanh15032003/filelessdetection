import sys
import numpy as np
import pandas as pd
import joblib
import ast

model = joblib.load('model.pkl')

with open('modified.txt', 'r') as file:
    content = file.read().splitlines()

numbers = [float(line) for line in content]


X=np.array([numbers])  # Example input array

predictions = model.predict(X)
print(predictions)
