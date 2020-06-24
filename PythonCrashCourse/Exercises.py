# What is 7 to the power of 4
a = 7 ** 4
print(a)

# Split a string into a list
string = "Hi there Sam!"
list_of_strings = string.split()
print(list_of_strings)

# Get the domain from an email

email = "mishalhajri96@gmail.com"
domain = email.split("@")[1]
print("The domain is ",domain)

smstring = "Is there a dog here? another dog is here what is dog bro"
mylist = []
a_list = lambda x,word: x.count(word)
print(a_list(smstring, 'dog'))



#filter words that does not start with letter s

def filterS(list):
    new_list = []
    for item in list:
        if item[0]=='s':
            new_list.append(item)

    return new_list

my_listt = ['soup', 'dog', 'salad', 'cat', 'great']
final_list = filterS(my_listt)
print(final_list)