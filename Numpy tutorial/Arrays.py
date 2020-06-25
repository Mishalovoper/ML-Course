import numpy as np

#Making a simple list then makes it an array

my_list = [1,2,3]
print(my_list)
print(np.array(my_list))
#This is a one dimensional array

#-------
#Making a 2D array you must have lists inside a list

mat_list = [[1,2,3],[4,5,6],[7,8,9]]
print(mat_list)
print(np.array(mat_list))

#Creating a list from range(start) to range(stop), using numpy arrays
#You can add step size in the third argument default 1

print(np.arange(0,10,3))


#Making an array of zeros
zeros = np.zeros(5) #Single argument means how many zeros you want
print(zeros)
zeros = np.zeros((5,5)) #If you pass in a tuple you can specify the dimension row, column
print(zeros)

# Same thing you can make ones array by using np.ones()

#--------------

#You can say I want an evenly spaced number from range to range arguments from,to, how many numbers you want
evenlyspaced = np.linspace(1,7,10)
print(evenlyspaced)


#Useful function for linear algebra problems eye() also called identity matrix, it has digonal 1s
print(np.eye(4))


#--------------
#Random values

#You can use np.random.anymethodavailable

#First method is to populate an array with random values from 0 to 1
print(np.random.rand(5))
print(np.random.rand(3,3)) #You can specify the dimension without passing a tuple


#You can get a random integer number by using low,high,how many numbers you want 1 is default

print(np.random.randint(0,2000,3))


#-----------

#Reshape method for changing the dimension of a an array

rarr = np.random.randint(0,900,10)
print(rarr)
new_array = rarr.reshape(2,5)
print(new_array)


#---------
#Good operations
print(rarr.max()) #Return max element
print(rarr.min()) #Returns min element
print(rarr.argmax(), rarr.argmin()) #Return the index of the max, min elements returns a tuple

#Getting a shape of an array simple use .shape() method
print(new_array.shape)
#Getting the datatype exists in your array
print(new_array.dtype)
