from matplotlib import pyplot as plt 
friends = [70, 34, 53, 94, 32, 98, 58, 38]
minutes = [175, 170, 205, 223, 123, 153, 232, 388]

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

plt.scatter(friends,minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,xy=(friend_count,minute_count), xytext=(5, -5), textcoords='offset points')

plt.title('Daily minutes vs Number of friends')
plt.xlabel('# of Friends')
plt.ylabel('daily minutes spent on the site')
plt.show()
