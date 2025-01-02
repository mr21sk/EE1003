import numpy as np
import matplotlib.pyplot as plt
import math

# Load data from the file
points = np.loadtxt('points.txt', delimiter='\t')  
x = points[:, 0]  
y = points[:, 1] 


# Plot the points
plt.figure(figsize=(10, 10)) 
plt.scatter(x, y, s=1, color='blue', alpha=0.5, label='Data Points')
plt.text(1, math.e , '(1, e)', fontsize=12, ha='right', va='bottom', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()






