##Numeric

print(1+1) #Simple Arithmetic Addition
print(1 * 3) #Multiplication
print(1/2) #Divison
print(2 ** 4) #Exponents
print(2 + 3 * 5 + 2) #Multiple operations
print(7 % 3) #Modulous

print("------------------")
print("")
### Assignment operator

a = 2
print(a)
x = 2
y = 5
print(x+y)


### Strings

print("-----------")

print("This i a String")
print("I can't go")
z = "Hello"
print(z)

age = 23
name = "Mishal"
# Printing multiple variables
print("My name is {}, and my age is {}".format(name, age))
#Or
print(print("My name is {one}, and my age is {two}, more {two}".format(one=name, two=age)))

print(name[len(name)-1])

# Slices
print(name[2:]) #Get values from index 2 and beyond
print(name[:3]) #Get values from beginning up to index 3 (But not including it)


# Lists

print("----------")

print([1,2,3])
print(['a','b','c'])
my_list = ['a', 'b', 'c']
print(my_list)
my_list.append('d') ##inserting an element to the list
print(my_list)
print(my_list[0]) #Grab a specific index
my_list[0] = 'AI' #Reassignig an element in a list
print(my_list)

#nested lists
nest = [1,2,[3,4]]

print(nest[2][0])

nest = [1,2,[3,4,['target']]]

print(nest[2][2][0]) ##Accessing a multi dimensional lists


