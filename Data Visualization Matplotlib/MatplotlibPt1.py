#Installing dependencies

import matplotlib.pyplot as plt
#This library works well with pandas and numpy
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2
#.plot() method will plot elements you pass

plt.plot(x,y)

#Define the x-axis label
plt.xlabel('X Label')
#Define the y-axis label
plt.ylabel('Y Label')
#Define a Title to the plot
plt.title('Title')
#plt.show()

#Create a subplot
#putting multiplot on the same canvas
#plt.subplot(rows,columns,plot number you are refering two)
plt.subplot(1,2,1)
plt.plot(x,y,'r') #Third argument is the line color
plt.subplot(1,2,2)
plt.plot(y,x,'g')
#plt.show()

#Object Oriented Method

fig = plt.figure()
print(fig)
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #Passing a list 4 arguments left,bottom,width,height range from 0 to 1
axes2 = fig.add_axes([0.7,0.15,0.2,0.2])
axes.set_xlabel('XLabel')
axes.set_ylabel('YLabel')
axes2.set_xlabel('YLabel')
axes2.set_ylabel('XLabel')
axes.plot(x,y)
axes.set_title('Bigger plot')
axes2.set_title('Smaller Plot')
axes2.plot(y,x)
plt.show()