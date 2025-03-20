# ================================== INDEXING WAY =============================
a = [1,2,3,4,5,6,7,8,9]
a[1] = 10
print(a)

# ================================== SLICING FOR MULTIPLE  =============================
b = [1,2,3,4,5,6,7,8,9]
b[1:4] = [21,31,41]
print(b)


# ================================== LIST COMPREHENSION WAY  =============================
c = [1,2,3,4,5,6,7,8,9]
# c_result = [x*2 if x%2==0 else x for x in c] #if you need every element
c_result = [x*2 for x in c if x%2==0] #if you need specific 
print(c_result)


# ================================== VIA ENUMERATE() =============================
e = [1,2,3,4,5,6,7,8,9]

for i, val in enumerate(e):
    # print(f"index is {i} and the value of index is {val}")
    if val % 2 != 0:
        e[i] += 10
print(e)


# ================================== via map() =============================
f = [1,2,3,4,5]
f_result = list(map(lambda x: x*2 , f))
print(f_result)

