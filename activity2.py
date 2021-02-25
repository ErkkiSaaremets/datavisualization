import numpy as np 
import matplotlib.pyplot as plt 

M = np.array([[1,1],[-2,2],[4,-7]])

print('Vector 1:')
print(M[0,:])
rows,cols = M.T.shape
print(cols)

k = 1

for i,k in enumerate(range(0,cols)):
    print("Iteration: {} - {}".format(i,k))
    print("Vector: {}".format(i))
    print(M[i,:])
    v1 = [0,0],[M[i,0],M[i,k]]
    print(v1)
    plt.figure(i)
    plt.plot(v1)
    plt.show()