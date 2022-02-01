# reshaping the array
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# displays the dimension of the array
print(arr.ndim)

# reshapes into 2D-ARRAY with 5-elements in each row
new_arr_1 = arr.reshape(2, 5)
print("2D-ARRAY",new_arr_1)

# reshapes into 3D-ARRAY with 3 elements in each row
new_arr_2 = arr.reshape(-1, 5, 2)
print("3D-ARRAY", new_arr_2)

# this new reshaped array returns the VIEW Array which means if original is changed the new array is also chamged
# returns original array if the ARRAY is VIEW
print(new_arr_2.base)
