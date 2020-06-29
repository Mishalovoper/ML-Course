import pandas as pd

sal = pd.read_csv('Salaries.csv')

print(sal.head())

print(sal.info())

print(sal['TotalPay'].mean())
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL'])
print(sal[sal['TotalPay']==sal['TotalPay'].max()])
print(sal[sal['TotalPay']==sal['TotalPay'].min()])

print(sal.groupby('Year').mean()['TotalPay'])

print(sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head(5))

print(sal[sal['Year']==2013]['JobTitle'].value_counts())

def checkIfContains(x):

    return 'chief' in x.lower()

print(sum(sal['JobTitle'].apply(checkIfContains)))