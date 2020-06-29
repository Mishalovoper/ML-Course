import pandas as pd
import numpy as np


#Group by is simply to group rows together based off a column and perform an aggregate function such as SUM


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','AMY','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

#Use group by lets say a company
print(df.groupby('Company'))
#Will return a group by object lets store it in a variable
byComp = df.groupby('Company')

#You can an aggregate function lets say the mean
print(byComp.mean())
print(byComp.sum())
print(byComp.std())

#If you want a specific row or a company for instance use:
print(byComp.mean().loc['FB'])

#You can use it all in one line
print(df.groupby('Company').sum())

#You can use count

print(df.groupby('Company').count()) #Look here its able to return the person all
print(df.groupby('Company').max()) #Return the max and min of each column in this group by

#You can use describe method to get useful information

print(df.groupby('Company').describe())

#You can use .transpose() method to make company as columns not rows

print(df.groupby('Company').describe().transpose())

