import matplotlib.pyplot as plt
import numpy as np

# lists to store data
xdata = []
ydata = []

# run through a range and randomly pick values to create sample datasets, then add them to lists for plotting
for i in np.arange(0,50,0.5):
    # add the values to the lists
    xdata.append(i)
    ydata.append(np.random.choice(100))

    

    # define the limits for the graph
    plt.xlim(-1,51)
    plt.ylim(-1,101)

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