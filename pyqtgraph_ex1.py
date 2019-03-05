# coding=utf-8
import pyqtgraph as pg
from pyqtgraph import QtCore
import numpy as np

app = pg.mkQApp()

win = pg.GraphicsWindow()
win.setWindowTitle(u'TEST')
win.resize(800, 300)

p = win.addPlot()
p.showGrid(x=True, y=True)
p.setRange(xRange=[0, 200], yRange=[-3, 3])

curve = p.plot(pen='g')
curve.setData(np.random.randn(200, ))

p2 = win.addPlot()
p2.setRange(xRange=[0, 200], yRange=[-60, 40])
c2 = p2.plot(pen='y')


def update():
	global curve
	data = np.random.randn(200, )
	curve.setData(data)
	c2.setData(10 * np.log(np.abs(np.fft.fft(data * (1 - data))))[:100])


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

app.exec()
