import pandas as pd
import dill
from sklearn.metrics import accuracy_score

df = pd.read_csv('data/mnist_test.csv', header=None)


X = df.drop(0, axis=1)
y = df[0]

with open('model/model.pkl', 'rb') as file:
    model = dill.load(file)

print(accuracy_score(y, model.predict(X)))
