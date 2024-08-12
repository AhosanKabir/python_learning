# We can use sets to get rid of duplicate items in other data structures like lists and tuples.

# set methods ----------------------->
one = {1,2,3,4}
two = {5,6,7}

result1 = one.union(two)
print(result1)
# same as union  The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
result2 = one | two
print(result2)

# update methods ----------------------->

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

result = set1.update(set2)
print("update --------------->>")
print(result)
print(set1)


# intersection -------------------- >>> 
set1 = {"apple" , "bananana", "cherry"}
set2 = {"google", " microsoft", "apple"}

result = set1.intersection(set2)
print("intersection")
print(result)

# intersection_update -------------------->
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

result = set1.intersection_update(set2)
print("intersection_update------------>>>>")
print(result) # give none, cause it's not return nothing
print(set1)


# Difference ------------------------------>
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

result = set2.difference(set1)
print("difference------------>>>>")
print(result)

# Symmetric Differences  ------------------------------>

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

result = set1.symmetric_difference(set2)
print("symmetric_difference------------>>>>")
print(result)

# ^ --------------------->

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(" ^------------>>>> ")
result = set1 ^ set2
print(result)

