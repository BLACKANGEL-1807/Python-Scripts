import matplotlib.pyplot as plott
import numpy as np

a = np.array(["v", "k", "y"])
b = np.array([11, 18, 16])

plott.bar(a, b, width=0.5)      # bar() takes width
plott.show()

# displays bar graph horizontally
plott.barh(a, b, color="green", height=0.5)    # barh() takes height
plott.show()
