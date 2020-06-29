import pandas as pd
import numpy as np

#If you have missing data, pandas will fill it as null or NaN data

#Will create a DataFrame out of a dictionary
#You can specify NaN value by using np.nan
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[6,7,8]}

df = pd.DataFrame(d)
print(df)

#Drop missing values, will drop anyrow that contains a NaN value
#Using df.dropna()

print(df.dropna()) #Axis is by default 0 which is rows
#You can drop any column that contains a NaN by providing axis=1 as an argument
print(df.dropna(axis=1))

#You can provide a threshold, which is simply the maximum NaN value contained if above or = maximum then will be dropped

print(df.dropna(thresh=2))

#You can fill out the missing values
#Using fillna() method
print(df.fillna(value='FILLED'))

#You can fill NaN values by the mean of the column

print(df['A'].fillna(value=df['A'].mean()))

