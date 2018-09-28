from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd

numpy.random.seed(2)

dataset = pd.read_csv("plessure.csv")
dataset.head()
X=dataset.iloc[:, 2:6]
Y=dataset.iloc[:, 1:2]
# print(Y)

model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu')) 
model.add(Dense(15, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid')) 

# WTF??????
# https://keras.io/getting-started/sequential-model-guide/#compilation
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(X, Y, epochs = 1000, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))