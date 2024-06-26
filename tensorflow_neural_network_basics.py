# -*- coding: utf-8 -*-
"""Tensorflow Neural Network Basics

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dkCTXKq8WzkZtzmIoDmWVZyKqb8RL4Qm

IMPORT DATA
"""

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/Churn.csv')

X = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis =1))
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.head()

y_train

"""Import Dependencies"""

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score

"""Build model"""

model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(X_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics='accuracy')

"""Fit, Predict and Evaluate"""

import numpy as np
# Convert X_train and y_train to float32
X_train = X_train.astype(np.float32)
y_train = y_train.astype(np.float32)

model.fit(X_train, y_train, epochs=100, batch_size=32)

import pandas as pd
# Assuming X_test is your DataFrame
X_test = X_test.astype(float)

y_hat = model.predict(X_test)
y_hat = [ 0 if val <0.5 else 1 for val in y_hat]
y_hat

accuracy_score(y_test, y_hat)

