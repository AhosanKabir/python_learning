a = [1,2,3,45]

key = 9
flag = False

for val in a:
    if val == key:
        flag = True
        break
    
if flag:
    print(f"{key} exists in your list")
else :
    print(f"{key} doesn't exist in your list")