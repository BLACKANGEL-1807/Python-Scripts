import matplotlib.pyplot as plott
import numpy as np
from numpy import random

# plot-1
x = np.array([20, 89, 10, 80, 50, 89, 78, 21, 44, 32, 91, 34, 0, 59, 19])
y = np.array([90, 32, 21, 67, 89, 90, 43, 88, 43, 73, 89, 65, 21, 47, 44])
plott.subplot(1, 2, 1)
plott.scatter(x, y, color="Blue")
plott.title("PLOT-1")

# plot-2
x = np.add(x, y)
y = np.subtract(x, y)
plott.subplot(1, 2, 2)
plott.scatter(x, y, color="green")
plott.title("PLOT-2")
plott.show()

# plot-3
x = np.array([90, 44, 78, 21, 89, 36, 91, 72, 99, 6, 19, 20, 88, 65, 43])
y = np.array([67, 90, 23, 89, 22, 84, 99, 100, 102, 90, 100, 210, 110, 121, 130])
plott.subplot(1, 2, 1)
plott.scatter(x, y, color="Blue", alpha=0.5)     # alpha - adjusts transparency of the dots

x = np.add(x, y)
y = np.subtract(x, y)
plott.scatter(x, y, color="Green", alpha=0.5)
plott.title("PLOT-3")


# plot-4
x = np.array([90, 44, 78, 21, 89, 36, 91, 72, 99, 6, 19, 20, 88, 65, 43])
y = np.array([67, 90, 23, 89, 22, 84, 99, 100, 102, 90, 100, 210, 110, 121, 130])
sizes = random.randint(low=100, high=300, size=15)
plott.subplot(1, 2, 2)
plott.scatter(x, y, color="Blue", alpha=0.5, s=sizes)     # alpha - adjusts transparency of the dots

x = np.add(x, y)
y = np.subtract(x, y)
sizes1 = random.randint(low=100, high=300, size=15)
plott.scatter(x, y, color="Green", alpha=0.5, s=sizes1)
plott.title("PLOT-4")


plott.show()
