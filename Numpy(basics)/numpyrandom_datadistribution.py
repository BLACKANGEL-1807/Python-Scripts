"""
Data Distribution is the list of all possible values, and how often the value occurs in a set.

Probability density functions, means probability of values in a set

Random Distribution is a set of random numbers that follow a certain probability density functions.
"""

import numpy as np
from numpy import random

a = random.choice([1, 2, 3, 4, 5], p=[0.1, 0.1, 0.5, 0.2, 0.1], size=100)
print(a)

