# coding=utf-8
import pyqtgraph as pg
from pyqtgraph import QtCore
import numpy as np

SAMPLE_RATE = 44100

app = pg.mkQApp()

win = pg.GraphicsWindow()
win.setWindowTitle(u'TEST')
win.resize(800, 300)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0, 1024], yRange=[-3, 3])

curve = p.plot(pen='g')
curve.setData(np.random.randn(200, ))

p2 = win.addPlot()
p2.showGrid(x=True, y=True)
p2.setRange(yRange=[-60, 40])
c2 = p2.plot(pen='y')

f = 10


def update():
	global curve, f
	# data = 2 * np.random.rand(1024, ) - 1
	data = np.sin(2 * np.pi * f / SAMPLE_RATE * np.arange(0, 1024))
	# data = data + 0.25 * np.hstack((data[1:], [0])) - 0.4 * np.hstack((data[2:], [0, 0]))
	curve.setData(data)
	spec = np.fft.fft(data * np.hanning(len(data)), 8192) / len(data)
	spec = spec[:len(spec) // 2]
	c2.setData(10 * np.log(np.abs(spec)))
	f += 10


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

app.exec()
