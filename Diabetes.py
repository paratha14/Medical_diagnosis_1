# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h0r4RuTwm9Xs0kxbtEdlvrXeIhieI9mB
"""

import pandas as pd
import numpy as np

df= pd.read_csv('./DataSets/diabetes_data.csv')
df

#studying the data
print(df.describe())
print('\n', dir(df))
print('\n shape: ', df.shape)

#checking for null value
print(df.isna().sum())

#specifying the target and X values
X= df.drop(['Outcome'], axis=1)
target= df['Outcome']

print('shape of X is: ', X.shape)
print('\n shape of target is: ', target.shape)

#scaling of data
from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()
X_scaled= scaler.fit_transform(X)
print('shape of X_scaled is: ',X_scaled.shape)
print('\n type of X_scaled is: ',type(X_scaled))

#doing hyperparametre tunning for checking more suitable
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
model_params={
    'RandomForest':{
        'model': RandomForestClassifier(),
        'params':{
            'n_estimators': [2,4,6,8]
        }
    },

    'LogisticRegression':{
        'model': LogisticRegression(solver='liblinear',multi_class='auto'),
        'params':{
            'C': [2,4,6,8]
        }
    }
}

from sklearn.model_selection import GridSearchCV
scores=[]
for mn,mp in model_params.items():
  print(mn)
  print(mp)
  clf= GridSearchCV(mp['model'],mp['params'],cv=5,return_train_score=False)
  clf.fit(X_scaled, target)
  scores.append({
      'model':mn,
      'best_params':clf.best_params_,
      'best_score':clf.best_score_
  })
  result = pd.DataFrame(scores,columns=['model','best_score','best_params'])
result

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X_scaled, target, test_size=0.2, random_state= 20, stratify= target)
print(X_train.shape,',', y_train.shape)

#we will be using LogisticRegression for this

model= LogisticRegression()
model.fit(X_train, y_train)

# accuracy on training data
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Testing data : ', test_data_accuracy)

#creating a predicitive system:
input_data = (0,0,0,0,0,0,0,0)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have Diabetes')
else:
  print('The Person has Diabetes')

#importing the model
import pickle
filename = 'Diabetes_model.sav'
pickle.dump(model, open(filename, 'wb'))
# loading the saved model
loaded_model = pickle.load(open('Diabetes_model.sav', 'rb'))

