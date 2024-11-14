print("Hello world")

#Python indentation
if 5 > 2:
    print("Five is greater than two!")

#comments:
print("Hello, World") #This is a comment

"""
This is 
a multiline
comment
"""
print("Hello world")


#variable:
x = 5
y = "Hello world!"
print(x)
print(y)

x_1 = 4
x_1 = "Sally"
print(x_1)


#casting
x = str(3)
y = int(3)
z = float(3)


#get the data types
print(type(x))
print(type(y))
print(type(z))

#single and double quotation same
x = "John"
#is the same as
y = 'John'

#variables are case sensitive
A = "Sally"
a = 4
#a will not overWrite A

#variable name
myvar  = "John"
my_var = "John" 
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



#one value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple" ,"banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#output from variable
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python"
y = "is"
z = "awesome"
print(x+y+z)

# x = "Python"
# y = 1
# z = "awesome"
# print(x+y+z)

#global variable
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#global keyword
def myfunc():
 global x
 x = "fantastic"
 print("Python is " + x)

myfunc()

print("Python is " + x)
