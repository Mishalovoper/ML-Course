#Installing dependencies

import matplotlib.pyplot as plt
#This library works well with pandas and numpy
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

"""
#Create a subplot using the same OOP method
#nrows = is the number of rows, ncols = is the number of columns
fig,axes = plt.subplots(nrows=1,ncols=2)
#plt.tight_layout() #This will fix the overlapping issue
#In subplot you can specify the number of rows and columns

#Axes is just a list you can specify which axes you want to plot on it
axes[0].plot(x,y)
axes[1].plot(y,x)
#Also you can acess axes to set some attributes:
axes[0].set_title('Title 1')
axes[1].set_title('Title 2')
plt.show()
"""

#Creating a figure and play with its width, height , etc..
"""
fig = plt.figure(figsize=(5,5)) #figsize= pass a tuple (width,height), you can also pass a dpi
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
plt.tight_layout()
plt.show()
"""
"""
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(5,5)) #figsize= pass a tuple (width,height), you can also pass a dpi
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.show()
"""
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#Multi plot on same canvas
ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cube')
#To add a legend you should pass a label argument in the ax object for each plot
ax.legend(loc=0)
#Notice how legend somewhat overlap the plot
#So you should specify loc method, but there is a documentation in the website to know the code number
#On where to put for example 0, is best, 1 is upper right etc..
plt.show()



#Saving a plot
#On high quality formats such as png
#fig.savefig('my_fig.png')

#Using legends






