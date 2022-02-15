import numpy as np
import seaborn as sb
from numpy import random
import matplotlib.pyplot as plot

arr = np.array([1, 1, 1, 1, 6, 9, 21, 50])
a = random.binomial(arr, p=0.6)
print(a)

sb.distplot(arr, hist=True, kde=False)
plot.show()