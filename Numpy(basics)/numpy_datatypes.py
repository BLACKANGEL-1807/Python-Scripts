# displays datatype of the numpy array
import numpy as np

arr = np.array([[[11, 18, 23, 89, 90, 77], [21, 21, 32, 12, 76, 36]],
                [[19, 29, 55, 74, 91, 99], [34, 56, 66, 33, 22, 44]]])

print(arr.dtype)


arr1 = np.array([[["Vky", "vikram"], ["abc", "zyx"]], [["deadpool", "Ikaris"], ["Iron Man", "Captain America"]]])
# prints U16 because here the array contains a element of LENGTH=15 (Captain America)
print(arr1.dtype)

arr2 = np.array([[11, 18, 22, 33, 44, 55], [66, 77, 88, 99, 100, 111]], dtype="S")
print(arr2.dtype)

# converting array from one datatype to another by using a copy of the array
new_arr2 = arr2.astype('int64')
print(new_arr2.dtype)

# displays all elements in array instead for using multiple loops
print("printing all elements")
for x in np.nditer(arr):
    print(x)

for i, x in np.ndenumerate(arr):
    print("Index {} : Value{}".format(i, x))
