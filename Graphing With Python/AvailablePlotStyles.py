import matplotlib.pyplot as plt
import numpy as np

#print(plt.style.available)

# available style can be found in the matplotlib documentation:
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# to test the styles on your own, the list is as follows:
#
#'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background',
# 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind',
# 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted',
# 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
# 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10'
#
# only change the plt_style string, the code will update the title and style for you!
plt_style='classic'

# set the style type from above (this shouldn't be changed)
plt.style.use(plt_style)

# make a figure container to hold the subplots
fig, ax=plt.subplots()

# rng generator
rng=np.random.default_rng()
rints1=rng.random(100)

# x-axis values for all four graphs
x1=np.arange(0,10,0.1)

# define a scale value since rng.random only goes from 0 -> 1
# --scaling it to 10 will map .2 to 2, .5 to 5, etc-- 
scale_value = 10

# y-axis values for all four graphs
y1=rints1*scale_value

# set the axis labels
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

# set the graph title to the style chosen
ax.set_title(plt_style)

# plot the axes and data in a color
# available colors can be found in the matplotlib documentation:
# https://matplotlib.org/stable/gallery/color/named_colors.html
ax.plot(x1,y1,color='red')

# plot the figure
plt.show()