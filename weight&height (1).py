# -*- coding: utf-8 -*-
"""Weight&Height.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11DExA9kDuLxy1SY4do0df-1SbEfR4_dW
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('WeightHeight.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
dataset.head()

INT a = 2 + 4 * 6 - 8 / 4
SWITCH (a++)
  CASE 6 :
    print("A")
    BREAK
  CASE 7 :
    print("B")
    BREAK
  CASE 24 :
    print("C")
    BREAK
  CASE 25 :
    print("D")
    BREAK
  DEFAULT :
    print("E")
    BREAK 
END SWITCH

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Height vs Weight (Train Set)')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show

plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Height vs Weight (Test Set)')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show

from sklearn.metrics import r2_score
r2_score(y_test,y_pred)