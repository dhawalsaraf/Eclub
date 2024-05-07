import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split

scaler=StandardScaler()
data= load_breast_cancer()
X=data.data
y=data.target
scaler.fit(X)
X= scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.75, random_state =2)

def sigmoid(z):
    e=1.0/(1.0+ np.exp(-z))
    return e

def sigmoid_derivative(self, z):
    return self.sigmoid(z)*(1-self.sigmoid(z))

class LogR:
    def __init__(self,learning_rate,epochs):
        self.lr= learning_rate
        self.ep= epochs
    def fit(self, X,y):
        n_samples, n_features = X.shape
        y=y.reshape(-1,1)
        self.weight = np.random.randn(n_features,1)/np.sqrt(n_features)
        self.bias= np.random.randn(1,1)

        for i in range(self.ep):
            z=np.dot(X,self.weight)+self.bias
            y_pred=sigmoid(z)

            dw=-np.dot(X.T,y-y_pred)/n_samples
            db=-np.sum(y-y_pred)/n_samples

            self.weight -= self.lr*dw
            self.bias -= self.lr*db

    def predict(self,X):
        z = np.dot(X,self.weight) + self.bias
        y = sigmoid(z)
        for i in range(len(y)):
            if(y[i]>0.5):
                y[i]=1 
            else:
                y[i]=0
        return y  

Fun =LogR(learning_rate=0.7, epochs=4500)
Fun.fit(X_train,y_train)
y_pred=Fun.predict(X_test)

LR=LogisticRegression(penalty= None, max_iter=20000)
LR.fit(X_train,y_train)
y_comp=LR.predict(X_test)

print(accuracy_score(y_test,y_pred))
print(accuracy_score(y_test,y_comp))

print(confusion_matrix(y_test,y_pred))
print(confusion_matrix(y_test,y_comp))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))
print(classification_report(y_test,y_comp))
