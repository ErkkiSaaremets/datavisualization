import matplotlib.pyplot as plt

values = [82,75,24,14,67,62,75,78,71,32,98,78,82,87,56,32]

plt.hist(values,5, histtype='bar', align='mid', color='c',label='Test Score Data', edgecolor='black')
plt.legend()
plt.title('Histograms of score')
plt.show()