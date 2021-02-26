import matplotlib.pyplot as plt 
import random
import numpy as np 

#create random data

x = np.arange(0,10,1)
y = np.zeros_like(x)
y = [random.random()*5 for i in x]

#Calculating mean value

y_mean = [np.mean(y)]*len(x)
fig,ax = plt.subplots()

#Plot the mean val from given dataset

data_line = ax.plot(x,y,label='Data',marker='o')
mean_line = ax.plot(x,y_mean,label='Mean',linestyle='--')

#create legend
legend = ax.legend(loc='upper right')

plt.show()
