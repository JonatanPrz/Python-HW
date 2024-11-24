# Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.cos(x)

# Plotting coine Graph
plt.plot(x, y, color='green')
plt.show()

 # I have retrieved this code from the amazing geeks from
# https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/