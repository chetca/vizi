from struct import *
from matplotlib import mlab
import pylab
import sys
import numpy as np

def sma_filter(y,s=10):
    r = [ np.mean( y[i-s:i] ) for i in range(s,y.shape[0])  ]
    return np.array(r)

argv = sys.argv
print("Будет загружен файл " + argv[1])

input = open(argv[1], "rb")
data = input.read()
xlist = list(unpack('10000H', data))
xlist.remove(0)
x = np.array(xlist)
x_sma = sma_filter(x, 7)
max_x = max(xlist) + 50
min_x = min(xlist) - 50

ylist = mlab.frange (2, 10000)
pylab.plot (ylist, xlist)
pylab.axis([0, 500, min_x, max_x])
pylab.title("Пульсовый сигнал")
pylab.gca().invert_yaxis()
pylab.show()

ylist = np.array(mlab.frange (1, 9992))
pylab.plot (ylist, x_sma)
pylab.axis([0, 500, min_x, max_x])
pylab.title("Сигнал после SMA")
pylab.gca().invert_yaxis()
pylab.show()
