from struct import *
from matplotlib import mlab
import pylab
import numpy as np
import sys

def sma_filter(y,s=10):
    r = [ np.mean( y[i-s:i] ) for i in range(s,y.shape[0])  ]
    return np.array(r)

def wma_filter(y,s=10):
    w = [ i for i in range(s,0,-1) ] 
    d = 2.0/ (s*(s+1))
    r = [ np.sum( y[i-s:i] * w ) * d for i in range(s,y.shape[0])  ]
    return np.array(r)
    
argv = sys.argv
print("Будет загружен файл " + argv[1])

size = 10000

input = open(argv[1], "rb")
data = input.read()
xlist = list(unpack('10000H', data))
xlist.remove(0)
x = np.array(xlist)
x_sma = sma_filter(x, 7)
x_wma = wma_filter(x, 7)

max_x = max(xlist)
min_x = min(xlist)

#52 - 139 (длина - 87)

#разделение для примера волны
del xlist[1:52:1]
del xlist[87:9948:1]

#разделение для усреднённой чистой волны
x_clear = x_sma.tolist()
del x_clear[1:52:1]
del x_clear[87:9948:1]

ylist = np.array(mlab.frange (1, 87))
pylab.plot (ylist, xlist)
pylab.axis([0, 87, min_x, max_x])
pylab.title("Пример волны")
pylab.gca().invert_yaxis()
pylab.show()
ylist = np.array(mlab.frange (1, 87))
pylab.plot (ylist, x_clear)
pylab.axis([2, 80, min_x, max_x]) # что бы график шёл с 2 а не с 0
pylab.title("Усреднённая модель")
pylab.gca().invert_yaxis()
pylab.show()
ylist = np.array(mlab.frange (1, 9992))
pylab.plot (ylist, x_sma)
pylab.axis([5, 300, min_x, max_x])
pylab.title("Алгоритм sma")
pylab.gca().invert_yaxis()
pylab.show()

pylab.plot (ylist, x_wma)
pylab.axis([5, 300, min_x, max_x])
pylab.title("Алгоритм wma")
pylab.gca().invert_yaxis()
pylab.show()
#print(x_sma)