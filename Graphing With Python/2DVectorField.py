import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20,20,1)

y = np.arange(-20,20,1)

u,v = np.meshgrid(x,y)

field = (v,-u)

fig, ax = plt.subplots()

q = ax.quiver(x,y,*field)

plt.show()