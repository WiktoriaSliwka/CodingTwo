import numpy as np

v1 = np.array([1,4])
              
m = np.array([
    [2,0],
    [0,2]
])

print(np.matmul(v1,m)) #matmul = matrix multiplication 
#print(np.matmul(v1 @ m))  # does same thing as above
#print(m.shape)
#print(v1.shape)