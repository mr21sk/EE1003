import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
gradient_ascent = ctypes.CDLL('./points.so')

# Define argument and return types
gradient_ascent.gradient_ascent.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
gradient_ascent.gradient_ascent.restype = ctypes.c_double

# Call the gradient ascent function
start_x = 0.0
learning_rate = 0.1
max_iterations = 1000
maxima = gradient_ascent.gradient_ascent(start_x, learning_rate, max_iterations)

# Plot the function and the maxima
x = np.linspace(-5, 30, 500)
y = 24 * x - x**2

plt.plot(x, y, label="24x - x^2")
plt.scatter(maxima, 24 * maxima - maxima**2, color='red', label=f"Maxima (x={maxima:.2f})")
plt.title("Function and Maxima")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

