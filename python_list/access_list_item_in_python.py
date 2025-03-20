# ================================= BASIC WAY ================================
a = [10,2,3,4,5,6,7,8,9]
# access item 
print(a[0])
# access item from last 
print(a[-1])

# ================================== LIST COMPREHENSION WAY =============================
b = [ 1,2,3,5,6,7,8]
b_result = [item for item in b if item > 3]
print(b_result)

# ================================== LIST SLICING WAY =============================
#  The starting index is included, but the ending index is not.

c = [1,2,4,5,6,7,8]
c_result = c[1:4]
print(c_result)

# ================================== LIST LOOP WAY =============================
d = [1,2,3,4,5,6,7,8]
for i in d:
    print(i)
    

