import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Method 1 (np.dot)
result = np.dot(A, B)

# Method 2 (shortcut)
result2 = A @ B

print(result)
# [[19 22]
#  [43 50]]
