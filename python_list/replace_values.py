
# ===================== Basic  WAY =============================

a = [1,2,3,4,5,6,7]
a[2] = 10
print(a)



# ====================== using lambda =============================

b = [1,2,3,4,5,6]
b_result = list(map(lambda x:99 if x==4 else x, b)) 
print(b_result)


# ================================== Using for loop =============================

c = [1,2,3,4]
for i in range(len(c)):
    # print(i)
    if c[i] == 2:
        c[i] = 44
print(c)


# ================================== using while loop =============================

d = [1,2,3,4,5]
i = 0

while i < len(d):
    # print(i)
    if d[i] == 3:
        d[i] = 45
    i += 1
    print(i)
print(d)

