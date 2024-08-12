# A tuple is a collection which is ordered and unchangeable.
# Ordered
# Unchangeable
# Allow Duplicates

thistuple = ("apple", "Banana", "Cherry")
print(thistuple[1])
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


checkTupple = ("apple", "banaana", "chili")
if "apple" in checkTupple:
	print('yes "apple" is in the fruits tuple')
else:
	print("'apple' is not in the fruits tupple")

# Add Items
addItemsOnTupple = ("a","b","c")
y = list(addItemsOnTupple)
print(type(y))

y.append("d")
add = tuple(y)
print(add)

# unpackging 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# loop in tupple 

thistuple = ("apple", "banana", "cherry")
print(" loopes result------------------->>") 
for x in thistuple:
	print(x)

thistuple = ("apple", "banana", "cherry")
print(" loopes result with range------------------->>")
for i in range(len(thistuple)):
  print(i)
  print(thistuple[i])

# count 
countTupple = ("a" ,"b","c","a","c","a")
print(" count tupple values ------------------->>")
print(countTupple.count("a"))