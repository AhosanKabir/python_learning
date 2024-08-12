# 1) String capitalize() Method  ----------------------------- >>
txt = "string"
captitalize_string = txt.capitalize()
print(captitalize_string)

# 2) String casefold() Method ----------------------------------- >>
# it will convert characters into lower case
txt = "STRING"
lowercase_string = txt.casefold()
print(lowercase_string)


# 3) String center() Method ----------------------------------- >>
# string.center(length->must needed , character->optional)
txt = "banana"
center_string = txt.center(20)
print(center_string)

# 4) String count() Method ---------------------------------- >>
# string.count(value -> must need, start->optional, end-> optional)
# Return the number of times the value appears in the string

txt = "I love apples, apple are my favorite fruit"
count_value_inside_string = txt.count("apple")
print(count_value_inside_string)

# 5) String encode() Method  ---------------------------------- >>
txt = "My name is Ståle"
encoded_text = txt.encode()
print(encoded_text)


# 6) String endswith() Method -------------------------- >>
# The endswith() method returns True if the string ends with the specified value, otherwise False.
txt = "Hello, welcome to my world."
end_with_string = txt.endswith(".") #true
end_with_string2 = txt.endswith("world") #false
end_with_string3 = txt.endswith("world.") #true
print(end_with_string, end_with_string2, end_with_string3) 

# 7) String expandtabs() Method ------------------------------ >>
# The expandtabs() method sets the tab size to the specified number of whitespaces.
txt = "H\te\tl\tl\to"
string_with_spacing =  txt.expandtabs(2)
print(string_with_spacing)

# 8) String find() Method --------------------------- >>
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
txt = "Hello, welcome to my world."
find_index_from_string = txt.find("welcome")
print(find_index_from_string)

# 9) String format() Method  --------------------------- >>
txt = "For only {price:.2f} dollars!" # .2f --> two-decimal format
string_formatting = txt.format(price = 49)
print(string_formatting)

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1, txt2, txt3)

# 10) String isalnum() Method ----------------------------- >>
string_with_gap = "company 12"  #false 
string_with_no_gap = "company12"  #true
out1 = string_with_gap.isalnum() 
out2 = string_with_no_gap.isalnum()
print(out1 , out2)


# 11) String isalpha() Method ------------------------------------- >>
# Check if all the characters in the text are letters:
is_alpha_1 = "CompanyXYZ".isalpha() #true cause all are letters
is_alpha_2 = "CompanyXYZ1234".isalpha() #false cause all are not numbers
print(is_alpha_1, is_alpha_2)

# 12) String isascii() Method  ------------------------------------ >>
# The isascii() method returns True if all the characters are ascii characters  (a-z).
# ASCII contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special characters.
is_ascii_1 = "compnay23er".isascii() #true
is_ascii_2 = "compnayaysdg".isascii() #true
print(is_ascii_1, is_ascii_2)


# 13) String isdecimal() Method ------------------------------------ >>
# The isdecimal() method returns True if all the characters are decimals (0-9).
is_decimal_or_not_1 = "1234".isdecimal() #true
is_decimal_or_not_2 = "1234asdfa".isdecimal() #false
print(f"is decimal or not----> {is_decimal_or_not_1 , is_decimal_or_not_2}")

# 14) String isdigit() Method --------------------------------- >>
txt = "50800asd"
x = txt.isdigit()
print(x)

# 15) String isidentifier() Method -------------------- >>
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

is_valid_or_not_1 = "valid".isidentifier() #true
is_valid_or_not_2 = "Not valid".isidentifier() #false
is_valid_or_not_3 = "23valid".isidentifier() #false 
is_valid_or_not_4 = "valid23".isidentifier() #true
print(is_valid_or_not_1, is_valid_or_not_2, is_valid_or_not_3, is_valid_or_not_4)


# 16) String islower() Method ----------------------------------- >>
# The islower() method returns True if all the characters are in lower case, otherwise False.Numbers, symbols and spaces are not checked, only alphabet characters.
is_lower_case_1 = "hello world".islower()  #true
is_lower_case_2 = "hello World".islower()  #false
print(is_lower_case_1, is_lower_case_2)

# 17) String istitle() Method -------------------------------- >>
# Check if each word start with an upper case letter:
is_each_word_uppercase_1 = "Hello, And Welcome To My World!".istitle() #true
is_each_word_uppercase_2 = "Hello, And Welcome to my World!".istitle() #false
is_each_word_uppercase_3 = "23 Hello, And Welcome To My World!".istitle() #true number not fact
print(is_each_word_uppercase_1, is_each_word_uppercase_2, is_each_word_uppercase_3)

# 18) String join() Method ------------------ >>
# The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = " and ".join(myTuple)
print(x)

# 19) String lstrip() Method -------------------------------- >>
# Remove spaces to the left of the string:

txt = "     ahosan          "
x = txt.lstrip()
print(x) 
print("Hello",x,"!")

# 20) String partition() Method -----------------------------  >>
txt = "I could eat bananas all day"
x = txt.partition("bananas") #tupple
print(x)

# 21) String replace() Method --------------------------------- >>
# Replace all occurrence of the word  
# string.replace(oldvalue, newvalue, count)
txt = "one one was a race horse, two two was one too.".replace("one", "three")
print(txt)

texts = "one one was a race horse, two two was one too."
x = texts.replace("one", "three", 2)
print(x)

# 22) String rsplit() Method ------------------------------- >>
# The rsplit() method splits a string into a list, starting from the right.
txt = "apple, banana, cherry"
y= txt.split(", ")
x = txt.rsplit(", ", 1)
# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.
print(x, y)

# 23) String strip() Method --------------------------------- >>
txt = "     pomegranate     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

removeletters = ",,,,,rrttgg.....banana....rrr"
x = removeletters.strip(".,tgr")
print(x)

# 24) String swapcase() Method ------------------------------- >>
txt = "Hello My Name Is AhOsaN"
x = txt.swapcase()
print(x)