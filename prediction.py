#!/usr/bin/python3
import sys
import numpy as np
import pandas as pd
import joblib
import ast
# Load the trained model
model = joblib.load('model.pkl')


import ast

# Read the file
with open('modified.txt', 'r') as file:
    content = file.read().splitlines()

# Process the numeric values
numbers = [float(line) for line in content]





# Convert the string representation to a list
#array = ast.literal_eval(content)


# Input data for prediction
X=np.array([numbers])  # Example input array

# Make predictions
predictions = model.predict(X)

# Print the predictions
print(predictions)
