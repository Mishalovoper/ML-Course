#Map
# Map is a function which saves the time
# you give it a list, and a function to perform an operation on each list item

listy = [1,2,3,4,5]

def mulByTwo(arg):
    return arg*2

new_list = list(map(mulByTwo,listy))
print(new_list)


#Lambda is also a time saver
# It can turn the above function into a single line
# lambda arg: args*2
# lambda argument: what is returns
i = lambda x : x *2
print(i(2))


#To check if in an element inside a list or not you can simply use:

a_list = [1,2,3,4]
print('x' in a_list)
print(1 in a_list)


#Tuple unpacking
# Where you have a tuples inside a list and you want to grab these values

tlist = [(1,2),(3,4),(5,6)]

for item in tlist:
    print(item)

    #this will print the tuple


for (item1,item2) in tlist:
    print(item1,item2)