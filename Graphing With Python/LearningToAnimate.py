import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.units as units
import numpy as np
from basic_units import radians

# lists to store data
xdata = []
ydata = []

# run through a range and randomly pick values to create sample datasets, then add them to lists for plotting
for i in np.arange(-2*np.pi,2*np.pi,0.1):
    # add the values to the lists
    xdata.append(i)
    ydata.append(np.sin(i))

    # define the limits for the graph
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-1.25,1.25)

    ax = plt.axes
    ax.plot(xunits=radians)

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