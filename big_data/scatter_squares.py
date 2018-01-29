import math
import matplotlib.pyplot as plt

x_val = list(range(1, 10000))
y_val = [math.tan(i) for i in x_val]

plt.scatter(
    x_val,
    y_val,
    s=2,
    edgecolor='none'
    , c=y_val
    , cmap=plt.cm.Blues
)

plt.axis([0, 1000, -10, 10])
plt.show()
