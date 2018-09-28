from struct import *
from matplotlib import mlab
import pylab
import sys

argv = sys.argv
print("Будет загружен файл " + argv[1])

input = open(argv[1], "rb")
data = input.read()
xlist = list(unpack('10000H', data))
xlist.remove(0)
max_x = max(xlist) + 10
min_x = min(xlist) - 10

ylist = mlab.frange (2, 10000)
pylab.plot (ylist, xlist)
pylab.axis([0, 300, min_x, max_x])
pylab.title("Пульсовый сигнал")
pylab.show()