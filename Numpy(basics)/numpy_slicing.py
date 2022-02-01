# numpy array slicing remains same  for the 1D-ARRAY like that of the normal list
# numpy array slicing for the 2D-ARRAY and greater dimensions are proceeded down below

import numpy as np

# #################### 2D-ARRAY ##################
print("#################### 2D-ARRAY ##################")

arr1 = np.array([[11, 18, 22, 33, 44, 55], [66, 77, 88, 99, 100, 111]])

# prints dimension of the array
print(arr1.ndim)

# print the elements
print(arr1[0, :2])

print(arr1[1, -1:-4:-1])


# ############ 3D-ARRAY ###################
print("############ 3D-ARRAY ###################")

arr = np.array([[[11, 18, 23, 89, 90, 77], [21, 21, 32, 12, 76, 36]],
                [[19, 29, 55, 74, 91, 99], [34, 56, 66, 33, 22, 44]]])

# prints Dimension of the array
print(arr.ndim)

# prints all the element at index (1,1)
print(arr[1, 1, :])

# prints the elements at (0,0)
print(arr[0, 0, :2])
