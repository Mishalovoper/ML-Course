
#For loops

seq = [1,2,3,4,5]

for item in seq:
    print(item)
    
    
#While loop

i = 1

while i < 5:
    print("i is {}".format(i))
    i = i +1


# For with range

#For in range(from,to)

for i in range(0,5):
    print(i)

#Range also can generate you a list

my_list = list(range(0,5))
print(my_list)


#Range for making changes in a list

for i in range(len(my_list)):
    my_list[i] = my_list[i]+1

print(my_list)

#Making a new list with some changes

new_list = [i+1 for i in my_list]
print(new_list)

#-----------

#Functions
def my_function(param1):
    print(param1)

my_function("Hi")

#Making a default name of a parameter if you do not pass any parameters

def a_function(name="Default"):
    print("Hello, "+name)

a_function()


# A function with return

def square(num=0):
    return num**2

output = square(2)
print(output)

# Adding a multiple line comment

"""
This is a multiple
line
comment
"""



