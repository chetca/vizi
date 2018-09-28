from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd
from struct import *
from matplotlib import mlab
import pylab

numpy.random.seed(2)

dataset = pd.read_csv("plessure.csv")
files = dataset.iloc[:, 0:1].values
# print(dataset)
uncode = pd.DataFrame({}, index = range(0, 10000))
for file in files:
    #print(file[0])
    input = open(file[0], "rb")
    data = input.read()
    xlist = list(unpack('10000H', data))
    df = pd.DataFrame(xlist, index = range(0, 10000))
    uncode[file[0]] = df

print(uncode['w486'].values)
