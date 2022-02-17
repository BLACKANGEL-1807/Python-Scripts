import matplotlib.pyplot as plott
import numpy as np

# In subplot(), here, totally 2-rows, 2-columns, third argument denotes the position

'''
NOTE: ALL THE LABELS SHOULD BE BELOW OR AFTER THE PLOT() STATEMENT
'''

# plot-1
x = np.array([10, 12, 78])
y = np.array([44, 32, 78])
plott.subplot(2, 2, 1)
plott.plot(x, y)
plott.title("PLOT-1")
plott.xlabel("x-axis")
plott.ylabel("y-axis")


# plot-2
x = np.array([90, 65, 1])
y = np.array([1, 2, 3])
plott.subplot(2, 2, 2)
plott.plot(x, y)
plott.title("PLOT-2")
plott.xlabel("x-axis")
plott.ylabel("y-axis")

# plot-3
x = np.array([42, 56, 83])
y = np.array([11, 89, 43])
plott.subplot(2, 2, 3)
plott.plot(x, y)
plott.title("PLOT-3")
plott.xlabel("x-axis")
plott.ylabel("y-axis")


# plot-2
x = np.array([21, 90, 33])
y = np.array([78, 90, 11])
plott.subplot(2, 2, 4)
plott.plot(x, y)
plott.title("PLOT-4")
plott.xlabel("x-axis")
plott.ylabel("y-axis")

plott.show()
