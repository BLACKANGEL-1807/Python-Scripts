import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr.ndim)
print(arr.shape)
print(arr)
print(arr.flatten())

for i in range(2):
    for j in range(2):
        for k in range(3):
            print(arr[[i], [j], [k]])

# prints the last element of the 3d Matrix
print(arr[1, 1, -2])
