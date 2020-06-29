import numpy as np
import pandas as pd
import os

d = {'col1':[1,2,3,4],
     'col2':[444,555,666,444],
     'col3':['abc','def','ghi','xyz']}
df = pd.DataFrame(d)
print(df)

#Finding unique values in a DataFrame
#You can specify a column you want to get unique value from
print(df['col2'].unique()) #Return a numpy array
#To get the number of unique value use .nunique()
print(df['col2'].nunique())

#You can count how many number appears in the list of number in specific column
print(df['col2'].value_counts())

#apply function is very useful, you provide a function to do some operations and apply it on specific column

def times2(x):
    return x*2

print(df['col1'].apply(times2))

#You can return a Series by the length of each string

print(df['col3'].apply(len)) # will return the length of each string to a new column

#You can use lambda expression
print(df['col1'].apply(lambda x:x*2))


#Removing a specific column

#df.drop('col1',axis=1,inplace=True)
print(df)

#Sorting a DataFrame by specific column

print(df.sort_values('col2'))


#to know if each value is null or not you can use df.isnull()
#Will return a DataFrame of boolean
print(df.isnull())


