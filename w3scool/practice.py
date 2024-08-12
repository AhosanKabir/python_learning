strings = "Hello world!"
print(strings)

# variables ::
x = 10
y = "john"
print(x)
print(y)

print(type(x))
print(type(y))

# many values to multiple :
x, y, z = "Orange", "Banana", "Cherry"
el = "Orange", "Banana", "Cherry"
el_1 = { "Orange", "Banana", "Cherry"}
el_2 = ["Orange", "Banana", "Cherry" ]
el_3 = [{"Orange", "Banana", "Cherry"},{"Apple", "Berry"}]
el_4 = {"name": "Ahosan", "age": 25}
a, b = el_3
c = True
print(x)
print(y)
print(z)
print(el)
print(type(el)) # tuple
print(type(el_1))
print(f"object--------------->{type(el_1)}") # set
print(type(el_2))
print(f"Array--------------->{type(el_2)}") # list
print(type(el_3))
print(f"Array of Objects--------------->{type(el_3)}") # list
print(type(el_4))
print(f"list of Objects--------------->{type(el_4)}") # dict
print(type(a))
print(type(b))
print(type(c))

# bonding output
X = "Python"
Y = "is"
Z = "awesome"
print(X,Y,Z)


# Global Variables
d = "awesome" #global variable
def myfunc():
  d = "fantastic" #block variable
  print(f"Python is ----------------------->{d}") #block scope
myfunc() 
print(f"Python is ----------------------->{d}") #global scope


# random numbers ==================>>>>
import random
print(random.randrange(1, 10))
print(random.randint(2,5))
# print(dir(random))


# all about string ==================>>>>>>>>

text = "Hello, Bro"
print(text[0])
print(len(text))
print ("hello" in text)
print ("Hello" in text)

if "Hello" in text :
  print("you are succesfully find")

if "hello" not in text:
  print("you got the point of not logic")

text2 = "Hello Ahosan !"
print (text[1:4])
print (text[3:])
print(text2.replace("Ahosan" , "Riad"))

text3 = "Honesty, Good Character , Truthfulness"
listOfText3 = text3.split(",")
print(listOfText3)
print(listOfText3[1])

upperCase = "uppercase"
lowerCase = "LowErCasE"
text_with_spaces = "   Text with whitespaces" # remove space from start (not middle)

print(upperCase.upper())
print(lowerCase.lower())
print(text_with_spaces.strip())

# for ele in text:
#   print(ele)


# string with number  ==================>>>
age = 25
txt = "Your age is {}"
#this gives us error
#print( txt + age) 
print(txt.format(age)) 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorders = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity, itemno, price))
print(myorders.format(quantity, itemno, price))