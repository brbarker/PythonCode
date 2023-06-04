import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# lists to store data
xdata = []
ydata = []

# run through a range and randomly pick values to create sample datasets, then add them to lists for plotting
for i in range(1,100):
    # add the values to the lists
    xdata.append(i)
    ydata.append(np.random.choice(100))

    # define the limits for the graph
    plt.xlim(0,100)
    plt.ylim(0,100)

    # plot the graph with the axis shown and the grid lines shown
    plt.plot(xdata,ydata,color='red')
    plt.axis('on')
    plt.grid(True)
    # make a title for the graph
    plt.title('A Living Graph')

    #pause between points to give the effect of animation
    plt.pause(0.05)

# show the graph
plt.show()