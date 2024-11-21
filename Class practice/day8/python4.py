#Loop through a list
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print('Loop through a list', x)

#Loop through the index number
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print('Loop through the index number', thisList[i])

#using a while loop
thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print('using a while loop', thisList[i])

    i = i + 1

#Looping using list comprehension
thisList = ["apple", "banana", "cherry"]
[print(x) for x in thisList]

#original
fruits = ["apple", "banana", "cherry", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

#using list comprehension

fruits = ["apple", "banana", "cherry", "mango"]

newList = [x for x in fruits if "a" in x]
print(newList)

#syntax

#newList = [expression for item in iterable if condition == true]
fruits = ["apple", "banana", "cherry", "mango"]
newList = [x for x in fruits if x != "apple"]
print(newList)
newList = [x for x in range(10)]
newList = [x if x != "banana" else "orange" for x in fruits]

#sort list automatically
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)


thisList = [100, 34, 56, 23]
thisList.sort()
print(thisList)

#sort descending
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse = True)
print(thisList)

#customize sort function
#sort the list based on how close the number is to 50
def myFunc(n):
    return abs(n - 50)

thisList = [100, 34, 56, 23]
thisList.sort(key = myFunc)
print(thisList)

#case insensitive sort of the list
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(key = str.lower)
print(thisList)

#reverse order
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.reverse()
print(thisList)

#use the copy method
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)

#use the list method
thisList = ["apple", "banana", "cherry"]
myList = list(thisList)
print(myList)

#use the slice operator
thisList = ["apple", "banana", "cherry"]
myList = thisList[:]
print(myList)

#join the lists
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]

for x in list2:
    list1.append(x)

print(list1)

#use the extend to add list2
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]

list1.extend(list2)
print(list1)


