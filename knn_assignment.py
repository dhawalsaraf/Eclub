import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter
import numpy as np

df = pd.read_csv("C:/Users/dmags/OneDrive/Desktop/study material/Eclub/glass.csv")
x= df.drop(columns='Type')
y= df['Type']
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8)

def dist(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))
class KNN(object):
    def __init__(self,k):
        self.k=k
    def fit(self,x_train, y_train):
        self.x_train=x_train
        self.y_train=y_train
    def predict(self,x_test):
        prediction=[self._helper(x) for x in x_test]
        return prediction
    def _helper(self,x):
        proximity=[dist(x,t) for t in x_train]
        indx=np.argsort(proximity)[:self.k]
        labels=[self.y_train[i] for i in indx]
        c=Counter(labels).most_common()
        return c[0][0]

def accuracy(prediction,y_test):
    return np.sum(prediction==y_test)/len(y_test)

K=KNN(k=7)
x_train=np.array(x_train)
y_train=np.array(y_train)
x_test=np.array(x_test)
y_test=np.array(y_test)

K.fit(x_train,y_train)
predictions= K.predict(x_test)
print(accuracy(predictions,y_test))

from sklearn.neighbors import KNeighborsClassifier
comp=KNeighborsClassifier()
comp.fit(x_train,y_train)
y_pred=comp.predict(x_test)
print(accuracy(y_pred,y_test))
