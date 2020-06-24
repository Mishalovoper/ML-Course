# Dictionary
# Is a key value par

d = {'key1':'value1','key2': 123}

print(d['key1']) #print an element in the key (key1)
print(d['key2'])
# You could have the value as a list

d['key3'] = [1,2,3,]
print(d['key3'])
#Dictionary inside a dictionary is also possible
d['key4'] = {'keyX':[1,2,3]}
#Acessing nested dictionary
print(d['key4']['keyX'][0])


#------------------

#Booleans

# is simple True False values
t = True
f = False
nott = not t
print(t,f,nott)

#-----------

#Tuples

#Items in a tuples cannot be changed when assigned

tuple = (1,2,3)
print(tuple)
#tuple[0] = 5 This will not work because tuples does not support item assignment



# -----------

# Sets
# Sets contains only unrepeatable valeus means they have only unique values

set = {1,2,3,4,3,4}
print(set)
# use method add() to add an element
set.add(90)
print(set)


## -----------------------

# Operations
 # 1 > 2
 # 1 < 2

print(1>2)
print(1<2)
print(1>=2)
print(1<=2)
print(1==1)
print(1==2)
print(1!=2)
print('hi'=='bye')
print('hi'!='bye')

#-----------

#Logic

# AND OR NOT
print("Logic")
print(1<2 and 2<3)
print(1<2 or 2>3)


# If elif else
#----------

print("Conditional")

if 1 < 2:
    print("Cool")


if 1 == 2:
    print("first")
elif 3==3:
    print("middle")
else:
    print("last")

