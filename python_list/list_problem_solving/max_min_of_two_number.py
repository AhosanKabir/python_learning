# ================================== using max()=============================
a = 7
b = 6
print(max(a,b))
print(min(a,b))


# ================================== conditional =============================

a1 = 3
b1 = 4
if a1 > b1:
    print(f"{a1} is greate")
else :
    print(f"{b1} is greater")
    
# or 
a2 = 5
b2 = 7
res = a2 if a2 > b2 else b2
print(res)



# ================================== using sort =============================

lists = [1,56,7,9,23,2]
lists.sort()
print(lists)
print(lists[-1])
print(lists[0])