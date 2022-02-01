import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [7, 8, 9, 10, 11]], dtype=int)

name = "Array"
# displays the version of the numpy
print("numpy version {} ".  format(np.__version__))
# displays array size(total elements)
print(f'{name} size', arr.size)
# displays the shape of array with outer-count-elements &  inner-count-elements
print(f'{name} shape', arr.shape)
# displays type of array
print(f'{name} type', type(arr))
# displays total axes(dimensions) in array
print(f'{name} dimensions', arr.ndim)
# displays element data-type
print(f'{name} dtype', arr.dtype)
print("##########################################################")

print(np.zeros(10))
print(np.ones(10))
print(np.full(10, 1))
print(np.empty(0))

arr1 = np.full(10, 1)
for i in range(arr.size):
    print(arr1[i])

print("############################################################3")
# displays the ndarray in single dimension
print(arr.flatten())
