# Python List ----------------------------------------------------->>>>>>>>>>>>>>
# Python lists store multiple data together in a single variable.

# a list of three elements
ages = [19, 26, 29]
print(ages)

# The enumerate() function adds a counter to an iterable and returns it as an enumerate object (iterator with index and the value).
company = ["A", "B", "C"]
for index , name in enumerate(company):
	print("index is %s for company: %s" % (index, name))


companys = ["A", "B", "C"]
company_enumerate = enumerate(companys)
print(list(company_enumerate))
