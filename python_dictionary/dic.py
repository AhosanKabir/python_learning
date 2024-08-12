# Dictionaries are used to store data values in key:value pairs.

test = {
    "name": "ahosan",
    "age":26,
    "bod": 1998,
    "address": ["mirpur","pabna","Dhaka", "pallabi"]
}
print(test)

test["name"] = "Riad"
print(test)
print(len(test))

print(test["address"][2])
for address in test["address"]:
    print(address)

# change value 

createDic ={
    "name": "abc",
    "age":26,
    "class": 11,
    "subject": ["Bangla","English","Math", "Others.."]
}

print(f" without change value---------> {createDic}")
createDic.update({"class": 9})
print(f" after update dictionary value---------> {createDic}")
