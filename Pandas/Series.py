#Main datatype working with pandas
#Similar to numpy array

import pandas as pd
import numpy as np

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

# Use pd.Series(data=somedata) to turn it into a table
print(pd.Series(data=my_data))

#You can change the index by specifying the index data
print(pd.Series(data=my_data,index=labels))
#Or you can use without specifying parameters
print(pd.Series(my_data, labels))

#Quick ways for creating a Series

print(pd.Series(arr)) #By passing a numpy array

#Passing a dictionary, will automatically set keys as index
print(pd.Series(d))

#Series can hold a vareity of data types

#We can store for examples the labels

print(pd.Series(labels))

#It can even store the python built in function

print(pd.Series(data=[sum,len,print]))







#Grabbing an information from a Series

ser1 = pd.Series([1,2,3,4],index=['SA','GER','USA','JAPAN'])
ser2 = pd.Series([1,2,5,4], index=['SA','GER','Italy','JAPAN'])

#Accessing by giving the inded name
print(ser1['SA'])

ser3 = pd.Series(labels)
print(ser3[0])


#Add two Series together. It will match first the indexes values for the two Series if it exist in both it will add, if not it will set a NaN value
print(ser1+ser2)

