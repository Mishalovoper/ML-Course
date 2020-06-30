import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,11)
y = x ** 2


#Plot appearance

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#color of the line, you should put the name of the color for example, blue
#Or you can put RGB HEX CODE FOR EXAMPLE #FFFFFF
#Linewidth is the width of the line
#Alpha is how transparent is the line
#You can pass a line style for example dashed -- or steps or : etc..
#You can mark out the x in this case
"""
ax.plot(x,y,color='purple',linewidth=2,alpha=1,linestyle='-',marker='o',
        markersize=10,markerfacecolor='yellow',markeredgewidth=3,
        markeredgecolor='green')
        """
ax.plot(x,y,color='purple',lw=2,ls='--') #lw, ls are short cut for linewidth, linestyle
ax.set_xlim([0,1]) #limits the number of x axis to appear
ax.set_ylim([0,2]) #limits the number y axis to appear
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')
plt.show()