"""
Seaborn is a module in python that uses matplotlib module underneath to plot graphs of random distribution datas

"""

# Distribution Plot
import seaborn as sb
import matplotlib.pyplot as plot

sb.distplot([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 9], hist=True)
# distplot means distribution plot, takes array as input and plot a curve
plot.show()
