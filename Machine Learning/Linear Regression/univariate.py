import numpy as np
from matplotlib import pyplot as plt

# Read in .csv file
data = np.genfromtxt('./Mumbai.csv', delimiter=',')

# Extract columns 0, 1 which are the price of the house and the area of the house respectively
y, x = data[:, 0][1:], data[:, 1][1:]
x_normed = x / x.max(axis=0)
y_normed = y / y.max(axis=0)

# Plot data to visualize
plt.title('Housing Prices and Area in Bangalore')
plt.xlabel('Area of the House')
plt.ylabel('Price of the House')
plt.plot(x_normed, y_normed, 'bo')
plt.show()
