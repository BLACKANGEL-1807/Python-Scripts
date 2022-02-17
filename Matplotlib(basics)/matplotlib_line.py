import matplotlib.pyplot as plott
import numpy as np

xpoint_1 = np.array([1, 10, 500])
ypoint_1 = np.array([5, 11, 250])
xpoint_2 = np.array([89, 20, 32])
ypoint_2 = np.array([77, 21, 45])

plott.plot(xpoint_1, ypoint_1, xpoint_2, ypoint_2, marker="*", ls=':')
'''
ls - linestyle
c - color

refer more arguments and customization for plot in w3school or google 
'''
plott.show()
