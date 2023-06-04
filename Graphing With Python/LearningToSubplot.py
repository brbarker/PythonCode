import matplotlib.pyplot as plt
import numpy as np

# rng generator
rng=np.random.default_rng()
rints1=rng.random(100)
rints2=rng.random(100)
rints3=rng.random(100)
rints4=rng.random(100)

# x-axis values for all four graphs
x1=np.arange(0,10,0.1)
x2=np.arange(0,10,0.1)
x3=np.arange(0,10,0.1)
x4=np.arange(0,10,0.1)

# define a scale value since rng.random only goes from 0 -> 1
# --scaling it to 10 will map .2 to 2, .5 to 5, etc-- 
scale_value = 10

# y-axis values for all four graphs
y1=rints1*scale_value
y2=rints2*scale_value
y3=rints3*scale_value
y4=rints4*scale_value

# style selection - the different styles can be found online
plt.style.use('ggplot')

# make a figure container to hold the subplots
fig=plt.figure()

# define the subplots and where they go in the figure
# add_subplot(nrows,ncols,plot_number)
# plot_number reads left -> right, top -> bottom
plt1=fig.add_subplot(221)
plt2=fig.add_subplot(222)
plt3=fig.add_subplot(223)
plt4=fig.add_subplot(224)

# plot each of the subplots
# colors: r=red, b=blue, g=green, k=black
plt1.plot(x1,y1,color='r')
plt1.set_title('Plot 1 (221)')

plt2.plot(x2,y2,color='b')
plt2.set_title('Plot 2 (222)')

plt3.plot(x3,y3,color='g')
plt3.set_title('Plot 3 (223)')

plt4.plot(x4,y4,color='k')
plt4.set_title('Plot 4 (224)')

# adjust space between subplot
fig.subplots_adjust(hspace=.5,wspace=.5)

# plot the figure
plt.show()