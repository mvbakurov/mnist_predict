import pandas as pd
from sklearn.neural_network import MLPClassifier
#from sklearn.model_selection import train_test_split
import dill

df = pd.read_csv('data/mnist_test.csv', header=None)

X = df.drop(0, axis=1)
y = df[0]

mlp = MLPClassifier(hidden_layer_sizes=(100, 100))
mlp.fit(X, y)

with open('model/model.pkl', 'wb') as file:
    dill.dump(mlp, file)


test_number = 800


print(y[test_number])
print(mlp.predict(X.iloc[[test_number]]))