import numpy
import matplotlib.pylab as plt 

m = [[0.0, 1.47, 2.43, 3.44, 1.08, 2.83, 1.08, 2.13, 2.11, 3.7],
[1.47, 0.0, 1.5, 2.39, 2.11, 2.4, 2.11, 1.1, 1.1, 3.21],
[2.43, 1.5, 0.0, 1.22, 0.0, 3.45, 0.0, 3.13, 1.76, 2.46, 3.04, 2.28],
[1.08, 2.11, 2.69, 3.45, 2.22, 4.43]]

matrix = numpy.matrix(m)

print(matrix)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect("equal")
plt.imshow(matrix, interpolation='nearest', cmap=None)
plt.colorbar()
plt.title('Matrix Visual Representation')

plt.show()