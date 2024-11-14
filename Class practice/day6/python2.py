#number
x = 1    # int
y = 2.8   #float
z = 1j   #complex
print(type(x))
print(type(y))
print(type(z))

#
x = 1    
y = 3659872655566
z = -32857766

#int
print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10   
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#float can be in the form of scientific number
x = 35e3   
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#complex
x = 3+5j   
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#Type conversion
x = 1   
y = 2.8
z = -1j

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random number
import random

print(random.randrange(1, 10))

#python casting
x = int(1)  
z = float("3")  
x = str("s1") 

#Assigning multiple strings
a = """ lorem i dsgfefngh
fhrghwefh rfghfhfh 
ehgfggfug ggggh
"""
print(a)

#string as an array
a = "Hello, world!"
print(a[1])

#Looping through string
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print(len(a))

#check the string is either present
txt = "The best things in life are free!"
print("free" in txt) #in keyword
if "free" in txt:
    print("yes,'free' is present")

print("expensive"  not in txt)
if "expensive" not in txt:
    print("No,'expensive' is not present")


#slicing
b = "Hello, world"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
print(a.upper())
print(a.lower())

#remove white space
a = " Hello, World "
print(a.strip())

a = " Hello, World "
print(a.replace("H","J"))
print(a.split(","))

age = 36
txt = "My name is john, I am " + str(age)
print(txt)
#f-string in py3.6
age = 36
txt = f"My name is john, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#math operation
txt = f"The price is {20 + 59} dollars"
print(txt)

#boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

class myClass():
    def _len_(self):
        return 0
    
myObj = myClass()    
print(bool(myObj))

def myFunction():
    return True

print (myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")

else:
   print("NO!") 


