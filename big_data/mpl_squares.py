import matplotlib.pyplot as plt

input_values = range(1, 100)
squares = [i**2 for i in range(1, 100)]

plt.plot(input_values, squares, linewidth=1)

plt.title('Squares Numbers')

plt.show()