from matplotlib import pyplot
import random

x_values = [0, 1, 2, 3, 4]
y_values = [random.randint(0, 30) for elt in x_values]
print(y_values)
pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("values")
pyplot.xlabel("Time")
pyplot.title("The time graph")

pyplot.show()

