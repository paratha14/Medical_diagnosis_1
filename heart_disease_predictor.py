# -*- coding: utf-8 -*-
"""Heart_Disease_predictor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XpHR4LUleDDkm1eXjq0U1pRYjp-csu89
"""
#importing libraries 
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

df= pd.read_csv('./DataSets/heart_disease_data.csv')
print(df.head(10))

print(df.isna().sum())

print(df.describe())

print(df.shape)

target= df['target']
inputs= df.drop(['target'], axis=1)

print(target.shape)

print(inputs.shape)

inputs

#scaling the values
scaler= StandardScaler()
X_scaled= scaler.fit_transform(inputs)

print(X_scaled.shape)
print(type(X_scaled))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X_scaled, target, test_size=0.2,stratify= target, random_state=42)

print(X_train.shape,',',X_test.shape,',',y_train.shape,',',y_test.shape)

#Model creation
model= LogisticRegression()
model.fit(X_train, y_train)

yp= model.predict(X_test)

from sklearn.metrics import accuracy_score
#accuracy of train data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)

#accuracy of test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('\n Accuracy on Test data : ', test_data_accuracy)

input_data = (57,0,0,120,354,0,1,163,1,0.6,2,0,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)
print(input_data_as_numpy_array.dtype)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
print(input_data_reshaped.dtype)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

import pickle
filename = 'heart_disease_model.sav'
pickle.dump(model, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))