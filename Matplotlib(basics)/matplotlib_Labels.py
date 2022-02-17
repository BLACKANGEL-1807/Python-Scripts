import matplotlib.pyplot as plott
import numpy as np

xpoint1 = np.array([20, 44, 1, 90])
ypoint1 = np.array([1, 89, 44, 21])

plott.grid()    # Displays grid on the graph

plott.plot(xpoint1, ypoint1, marker="o")

plott.xlabel("array1")
plott.ylabel("array2")
plott.title("Summa oru array")


plott.show()
