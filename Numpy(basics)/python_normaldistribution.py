import seaborn as sb
from numpy import random
import matplotlib.pyplot as plot
import numpy as np

"""
loc - mean
scale - standard deviation

"""

a = random.normal(loc=5, scale=5, size=(20000, 1000))
print(a)
arr = np.array([[[11, 18, 23, 89, 90, 77], [21, 21, 32, 12, 76, 36]],
                [[19, 29, 55, 74, 91, 99], [34, 56, 66, 33, 22, 44]]])

# sb.distplot(arr, hist=False)
sb.distplot(a, hist=True, kde=True)
plot.show()
