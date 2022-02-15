"""
Permutation refers to the arrangement of elements.

e.g., [1,2,3] is a permutation of [3,2,1] and vice versa
"""

import numpy as np
from numpy import random

arr = np.array([[1, 2, 3], [4, 5, 6], [13, 14, 15], [7, 8, 9], [10, 11, 12], [16, 17, 18]])
print("Dimension: {}".format(arr.ndim))

random.shuffle(arr)  # shuffle changes the original array.
print(arr)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# permutation  doesn't change the original array
new_arr1 = random.permutation(arr1)
print(new_arr1)
