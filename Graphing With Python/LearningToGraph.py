import matplotlib.pyplot as plt
import numpy as np

# rng generator
rng=np.random.default_rng()
rints=rng.random(100)

# x-axis values
x1=np.arange(0,10,0.1)
x2=np.arange(0,10,0.1)

# define a scale value since rng.random only goes from 0 -> 1
scale_value = 10

# y-axis values
y1=rints*scale_value

#test prints
print(len(x1))
print(len(y1))

# find line of best fit (x-values,y-values,degree of polynomial for fit)
model=np.poly1d(np.polyfit(x1,y1,50))

# graph axis limits
#plt.xlim(0,10)
#plt.ylim(-1,10)

# plotting
plt.plot(x1,y1,label="Line 1")
plt.plot(x2,model(x2),label="Line 2")

# naming the x-axis
plt.xlabel('x-axis')

# naming the y-axis
plt.ylabel('y-axis')

# giving the graph a title
plt.title('A Graph')

# giving the graph a legend
plt.legend()

#prints the coefficients for each term of the fit polynomial
print(model)

# showing the plot
plt.show()

