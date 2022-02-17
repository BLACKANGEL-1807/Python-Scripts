import matplotlib.pyplot as plot
import numpy as np

xpoint = np.array([0, 6, 200])  # stores collection of X-points corresponds to Y-points
ypoint = np.array([0, 250, 40])  # stores collection of Y-points corresponds to X-points
# the coordinates are (0,0) (6,250) (200, 40)

plot.plot(xpoint, ypoint)
plot.show()

plot.plot(xpoint, ypoint, '*') # displays only points in the graph
plot.show()
