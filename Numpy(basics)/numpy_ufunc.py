import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

c = np.add(a, b)
print(c)

# creating a custom ufunc - universal functions
def add_2_str(v, k):
    y = v + k
    return y


add_2_str = np.frompyfunc(add_2_str, nin=2, nout=1)
print(add_2_str([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

print(add_2_str("Hie", "Hello"))
# displays it is a function class from numpy
print(type(add_2_str))
