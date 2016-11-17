# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:26:46 2016

@author: sharath
"""
# Variables
# a,b,c are integer variables
a = 5 # assignment operator
b = 6
c = -8

# d,e,f are floating point variables
d = 5.6
e = 9.0000e-4
f = -1.4

# Find out the type of a variable
print type(a)
print type(e)

# Boolean types - True and False are defined keywords in Python
True
False



# Operators
print (a + b)
print (c - d)
print (a * c)
print (a / b)
print (a % 2)
print (c ** a)
print (b // a)

x = 1
a = a + 1 # shorthand x += 1



# Conditions, make sure the indentation is correct
if b >= 5:
    print("if clause is true")        
elif b >= 3:
    print("elif clause is true")
else:
    print("else clause is true")

# conditional operators
#  ==  equal to
#  >   greater than
#  <   less than
#  >=  greater than or equal to
#  <=  less than or equal to
#  !=  not equal to



# Functions
def function_dummy_1():
    # This function does not accept any arguments
    # Function body that does something meaningful
    return 0 # return some results


def function_add(x, y):
    # This function accepts 2 arguments
    return x + y # return sum of the two arguments


def function_mul(a, b):
    # This function accepts 2 arguments, note that the a and b in the function
    # definition is not the same as the variables a and b
    return a * b # return product of the two arguments


# Scope of variables within functions
def function_dummy_2():
    # This function does not accept any arguments
    print y # y is not declared before and is not visible within the function
    return y # return some results


def function_dummy_3():
    # This function does not accept any arguments
    y = 10
    z = 15
    return True # return some results

print y, z # y and z are declared within the function, and are not visible outside



# Loops, note the indent
# whatever is indented is considered to be a part of the repeatable section 
# of the loop
for a in range(1, 4):
    print (a)
    
# range() generates a sequence of integers, often helpful for iterating over a
# series of items
print range(5, 10)
print range(5, 10, 2)
print range(5, 10, -2)
print range(10, 5, -2)

# Another way of looping in Python, note the increment step
# If you forget the increment step, this code will run forever printing values of u
u = 1
while u < 10:
    print (u)
    u+=1



# Strings
foo = "This is my string"
print foo
bar = "This is your string"
print bar
baz = "This is our string"
print baz
bat = 'We can use single quotes; this is also a string'
print bat
woot = 'We can "mix" quotes'
print woot
toot = "     We can 'mix' quotes like this too      "
print toot
zoot = 'People\'s Republic'
print zoot



# counts the number of occurrences of 'x'
print woot.count('x')
# returns the position of character 'x'
print foo.find('x')
# returns the stringVar in lowercase (this is temporary)
print foo.lower()
# returns the stringVar in uppercase (this is temporary)
print foo.upper()
# replaces all occurrences of 'my' with 'your' in the string
print foo.replace('my', 'your')
# remove preceeding and trailing spaces
print toot.strip()

# Slicing strings
print foo[0:4]
print foo[4:7]
print foo[4:]
print foo[:-1]
print foo[4:-1]
print foo[-5:]



# Lists
int_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print int_list

# iterating over list items
for item in int_list:
    print item, item**2

for idx in range(len(int_list)):
    print int_list[idx], int_list[idx]**2

# appends element to end of the list
int_list.append(16)
print int_list
# counts the number of occurrences of 4s in the list
int_list.count(4)
# returns the index of 10 in the list
int_list.index(10)
# inserts 4 at location 2
int_list.insert(2, 4)
print int_list
# returns last element then removes it from the list
int_list.pop()
print int_list
# finds and removes first 4 from list
int_list.remove(4)
print int_list
# reverses the elements in the list
int_list.reverse()
#sorts the list alphabetically in ascending order, or numerical in ascending order
int_list.sort() 

# Lists could also be sliced
# Strings could be interpreted as lists
for letter in foo:
    print letter

# replace multiple instances in lists - to do



t = (1, 2, 3)
print (t)
t.append(4) # will fail because tuples are immutable
print t[0], t[1], t[2]
t[0] = -1 # will fail because tupes are immutable




# Dictionaries
# Key value data structure, unordered - what you type in need not be the order
# in which the data gets stored
my_dictionary = {'name': 'Foo Bar',
                 'Age': -220,
                 'Profession': 'Jobless',
                 'Qualifications': 'Worthless'}

print(my_dictionary['Profession'])

# Iterating and accessing dictionary keys and values
for k in my_dictionary:
    print 'Key:', k, ', - Value:', my_dictionary[k]

# The dictionary data type provides in built methods to access keys and values
print my_dictionary.keys()
print my_dictionary.values()

# Another way of accessing keys and values from a dictionary
for key in my_dictionary.keys():
    print key, ' - ', my_dictionary[key]

# Adding a new key value pair
my_dictionary['IQ'] = -911
print my_dictionary

# Removing a key value pair
my_dictionary.pop('IQ')
# pop-ing a non-existent key will result in an error
my_dictionary.pop('IQ') # already pop-ed, cannot pop 'IQ' again

# Update a value for a key
my_dictionary['name'] = 'Foo Baz'




# References and copying objects, mutable types
# We had an int_list
# Let's create a new_list by assignment
new_list = int_list
print new_list
print int_list

# Let's change the first item of new_list
new_list[0] = -10
print new_list # nothing unexpected
print int_list # Why did the first item change here?

# For mutable composite data types, python creates references
# If another copy is reuqired, it must be explicitly created

import copy
new_list = copy.deepcopy(int_list)
new_list[0] = 1
print new_list
print int_list

# This behaviour is not applicable for basic data types like integers, floats etc.



my_input = input('Type in something: ')
print my_input, len(my_input)

my_raw_input = raw_input('Type in some more: ')
print my_raw_input, len(my_raw_input)

file_handle = open('temp.txt', 'w')
file_handle.writelines(['this is a string\n', 'this is another string\n'])
file_handle.close()

file_handle = open('temp.txt', 'r')
x = file_handle.readlines()
file_handle.close()

# there are the readline(), writeline() functions
# there are the read() and write() functions too



#enumerate
list_of_strings = ['aa', 'bb', 'cc', 'dd']

for idx, string in enumerate(list_of_strings):
    if idx%2 == 1:
        print idx, string




#generators

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print i




#importing modules, code organization etc.

# create folder, two files with classes, __init__ method and another method
# __init__.py file

# __name__ variable, significance


