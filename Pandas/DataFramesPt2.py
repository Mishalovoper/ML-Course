import numpy as np
import pandas as pd

from numpy.random import randn


np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Conditional Selection

#Same as numpy you can use df > 0 for instance, will return a dataframe of boolean

print(df>0)

#You can assign it condition to a variable, then pass it as a bracket argument to a dataframe, will return only the satisified condition values
#Others will be returned as NaN
booldf = df > 0

print(df[booldf])

#Or simply df[df>0]

#You can use condition for a specific Column lets say W
#Will return a Series of boolean values
print(df['W']>0)

#To not return a null values use df[df['W']>0]

print(df[df['W']>0])
#Getting mulitple columns out of these you can simply use it in one line

print(df[df['W']>0][['X','Y']])

#Multiple conditions

print(df[(df['W']>0) & (df['Y']>1)]) #using and here is not the way to deal with Series instead use &
#You can use OR operation by using |
print(df[(df['W']>0) | (df['Y']>1)])

#You can reset the index to be numerical rather than String by using df.reset_index()
#The labels will be inserted as a new column

print(df.reset_index())
#If you want it to occur on the original dataframe use inplace=True as an argument
#df.reset_index(inplace=True)

#Reset to a new index
newind = 'CA NY WY OR CO'.split()
print(newind)
df['States'] = newind
print(df)

#You can set a column as an index by using .set_index('column_name')
print(df.set_index('States'))


