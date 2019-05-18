from struct import *

import matplotlib
matplotlib.use("Agg")
 
# подключаем необходимые пакеты
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab
import argparse
import random
import pickle
import cv2
import os 

dataset = pd.read_csv("plessure.csv")
files = dataset.iloc[:, 0:1].values
# print(dataset[file[0]])
 
uncode = pd.DataFrame({}, index = range(0, 10000))
for file in files:
    print(file[0])
    input = open(file[0], "rb")
    data = input.read()
    xlist = list(unpack('10000H', data))
    df = pd.DataFrame(xlist, index = range(0, 10000))
    uncode[file[0]] = df

uncode = uncode.T
print(uncode)
print(dataset['upper'].values)

model = Sequential()
model.add(Dense(1024, input_shape=(10000,), activation="sigmoid"))
model.add(Dense(512, activation="sigmoid"))
model.add(Dense(dataset['upper'].values, activation="softmax"))

# https://keras.io/getting-started/sequential-model-guide/#compilation

INIT_LR = 0.01
EPOCHS = 75
 
# компилируем модель, используя SGD как оптимизатор и категориальную
# кросс-энтропию в качестве функции потерь (для бинарной классификации 
# следует использовать binary_crossentropy)
print("[INFO] training network...")
opt = SGD(lr=INIT_LR)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"]) 
model.fit(uncode.T, dataset['upper'].values, epochs=EPOCHS, batch_size=32)

scores = model.evaluate(uncode.T, dataset['upper'].values)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))