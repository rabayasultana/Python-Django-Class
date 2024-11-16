
#operator
print(10 + 5)
print((10 + 5) - (10 + 5))
print(10 + 5 * 3)

###list
thisList = ["apple", "banana", "cherry"]
print(thisList)


print(len(thisList))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5]
list3 =[True, False, True]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]

print(type(list1))

thisList = list(("apple", "banana", "cherry"))
print(thisList)
print(thisList[1])

thisList = ["apple", "banana", "cherry"]
print(thisList[1])
print(thisList[-1])

thisList = ["apple", "banana", "cherry", "orange", "Kiwi", "melon", "mango"]
print(thisList[2:5])
print(thisList[-4:-1])

thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("yes, apple")

#change item value
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

#change a range of item values
thisList = ["apple", "banana", "cherry", "orange", "Kiwi", "melon", "mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)

#if you insert less items
thisList = ["apple", "banana", "cherry"]
thisList[1:3] = ["watermelon"]
print("this is", thisList)

#insert new items
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)

#to add an item to the end
thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)

#add item of one list to another
thisList = ["apple", "banana", "cherry"]
tropical = ["flower1", "flower2", "flower3"]
thisList.extend(tropical)
print(thisList)

#remove specified item
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

thisList = ["apple", "banana", "cherry", "banana", "kiwi"]
thisList.remove("banana")
print(thisList)

#remove specified index
thisList = ["apple", "banana", "cherry"]
thisList.pop(1)
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)

#del
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

#del to delete entire list
thisList = ["apple", "banana", "cherry"]
del (thisList)

#clear the list
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

#Loop through a list
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

#loop through the index number
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(thisList[i])

thisList = ["apple", "banana", "cherry"]
i=0
while i < len(thisList):
    print(thisList[i])
    i = i+1

#
thisList = ["apple", "banana", "cherry"]
[print(x) for x in thisList]


fruits = ["apple", "banana", "cherry", "banana", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# newList = [x.upper() for x in fruits]
# print(newList)
# newList = [x if x != "banana" else "orange" for x in fruits]
# print(newList)


fruits = ["apple", "banana", "cherry", "banana", "kiwi", "mango"]
newList = []
i = 0

while i < len(fruits):
    newList.append(fruits[i].upper())
    i += 1

print(newList) 