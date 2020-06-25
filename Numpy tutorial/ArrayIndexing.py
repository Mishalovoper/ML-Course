import numpy as np

#Create a sample array

arr = np.arange(0,12)
print(arr)

#Getting a value from an array is as you get from a list

print(arr[2])

#Slices use [starting_index : end_index]

print(arr[0:5])

#from start upto some index u can use [:end_index]

print(arr[:4])

#Setting multiple values from an array to specific value
arr[0:5] = 100
print(arr)

#Assigning an array to another, any changes to any of the array going to reflect on the other
#You can use method .copy() to create a new copy.

slices = arr[0:4]
print(slices)
slices[:] = 2
print(slices)
print(arr)

# accessing a 2d array
#You can use arr_var[row][column] or arr_var[row,column]

# Slices of the 2d array can be grapped by arr_var[starting_row:ending by not including row,starting column: ending but not including column

arr_2d = np.arange(5,151,5).reshape(6,5)
print(arr_2d)
print(arr_2d[2:4,1:4])

#Conditional array
#You make condition based on the values here and returns an array of boolean values

arr_con = np.arange(1,11)
print(arr_con)
print(arr_con%2 == 0)#True if the specific value is bigger than 5 and false else
bool_array = arr_con%2 == 0
#If you want only the true values you can pass the array of booleans to the origin array bracket[]
print(arr_con[bool_array])

#Or in single line arr_con[arr_con>5]

