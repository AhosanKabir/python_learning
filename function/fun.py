# lambda arguments : expression 

# () passing value --------------------------- >
x = lambda x: x + 1
print(x(4))

x = lambda x , y : x * y
print(x(4,5))

# () direct calling ------------------------------ >
a = (lambda x: x*x*x)(2)
print(a)


# () for consice and expressive code ---------------------- >
    ##### map(function, iterables) , using lambda with map
numbers = [1, 2, 3, 4, 5, 6 ]
def square(numbers):
    return numbers * numbers
squared_numbers_default = list(map(square, numbers))

squared_numbers_with_lambda = list(map(lambda x : x*x, numbers))


print(f"without lambda ------------->{squared_numbers_default}")
print(f"without lambda ------------->{squared_numbers_with_lambda}")

    ##### filter(function, iterable) , using lambda with filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
            
    return even_numbers
print(f"even numbers------------->{check_even(numbers)}")

even_numbers_lambda = list(filter(lambda x : x % 2 == 0, numbers))
print(f"even numbers with lambda------------->{even_numbers_lambda}")




    ##### sort , using lambda with sorted

sort_numbers = [11, 2, 33, 4, 5, 36, 7, 18, 9, 10]

sorted_numbers = sorted(sort_numbers , key=lambda x: -x)
print(f"sorted numbers -----------------> {sorted_numbers}")