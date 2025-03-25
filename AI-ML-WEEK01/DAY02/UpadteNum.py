import numpy as np

A = np.array([[1,2,3],
			  [4,5,6],
			  [7,8,9]])

A[2,2] = 0
A[1,0]= 8

print(A)  
#ans [[1, 2, 3],
# [8, 5, 6],
# [7, 8, 0]]
