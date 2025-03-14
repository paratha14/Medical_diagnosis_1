# -*- coding: utf-8 -*-
"""Lung_Cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tBD4x-VCMXASoLqYMwuR3sDIM__J4VKB
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from sklearn.metrics import accuracy_score

#reading data into a dataframe
df= pd.read_csv('./DataSets/survey lung cancer.csv')
print(df.head(10))
#studying the data
print(df.describe(),'\n')
print('shape of df is: ',df.shape,'\n')
print('more info on the dataset: ', df.info())

#checking for null values:
print('Null values in the columns are as follows: \n',df.isnull().sum())

#LabelEncoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['GENDER']= le.fit_transform(df['GENDER'])
print('Values of GENDER after labelencoding: ',df['GENDER'].unique())
df['LUNG_CANCER']= le.fit_transform(df['LUNG_CANCER'])
print('\n target values or the lung_cancer values after labelencoding are: ',df['LUNG_CANCER'].unique())

# checking the distribution of Target Variable
df['LUNG_CANCER'].value_counts()
#1 - Defective Lungs
#0 - Healthy Lungs

#dividing the dataframe into X and Y componets
X = df.drop(columns='LUNG_CANCER', axis=1)
Y = df['LUNG_CANCER']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

#Model Training
model= LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Testing data : ', test_data_accuracy)

#creating a predicitive system:
input_data = (0,61,1,1,1,1,2,2,1,1,1,1,2,1,1)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Lung Cancer')
else:
  print('The Person has Lung Cancer')

#Saving the model
import pickle
filename = 'lungs_disease_model.sav'
pickle.dump(model, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('lungs_disease_model.sav', 'rb'))

