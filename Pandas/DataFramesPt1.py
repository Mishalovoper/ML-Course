import numpy as np
import pandas as pd

from numpy.random import randn


np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# Passing in a column name, it will returns the column content

print(df['W']) # will return a Series
#To confirm that its a series
print(type(df['W']))

#Data Frame is a punch of series

#Another way of accessing a column is by df.columnName

print(df.W) #It may get confused with a method with the same name

#Getting multiple columns by using df[['W','Z']] for instance

print(df[['W','Z']])

#Creating new column by doing a math operation, for instance:
df['Sum of W and Z'] = df['W']+df['Z']
print(df)


#Removing a column df.drop('columnName',1), this method will only return the new dataframe while not affecting the actualy df
#If you want to actually to delete it you specify inplace=True argument
#axis argument 0 refers to the rows 1 refers to the columns
print(df.drop('Sum of W and Z',1))
print(df)
df.drop('Sum of W and Z',1,inplace=True)
print(df)

#Removing a row you can specify the row name
print(df.drop('E',0))

#To know how many rows and column you have
#You can use df.shape method
print(df.shape)


#Selecting a row, use df.loc['rowLabel']
#Will return a series
print(df.loc['A'])
#Selecting row by index number use df.iloc[indexNumber]
print(df.iloc[2])

#To select a specific value from the dataframe
#Use df.loc['rowLabel', 'columnLabel']
print("-")
print(df.loc['A','W'])

#Taking a subset for example ROW A,B Values of W, Z
#Use df.loc[ [list_of_rows] , [list_of_columns] ]
print(df.loc[['A','B'],['W','Z']])