import numpy as np
from numpy import random

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# displays two random integer from 90 to 99
a = random.randint(low=90, size=2,  high=99)
# the result is a ND-ARRAY
print(a)

# passing ndarray for parameters of LOW and HIGH,
arr1 = np.array([[[30], [30], [40]], [[28], [27], [31]]])
b = random.randint(low=[1, 3, 5, 7],  high=arr1)
# the result array is determined by the LOW and HIGH
print(b)

# rand is used to generate a random FLOAT from range 0-1
c = random.rand(3)
print(c)

# displays FLOAT value from 0-1 with 3-ROWS each containing 5-elements
d = random.rand(3, 5)
print(d)

# display random single integer from the array given in params
e = random.choice([11, 18, 16, 21, 69])  # the parameter must be a 1-D array only
print(e)
