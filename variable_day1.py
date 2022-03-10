name = 10
print(name)
print(type(name))
print(id(name))

"type will give data type and id will give memory address"
"Variable rules" \
"1. start with AtoZ or atoz or underscore" \
"2. python is case sensitive e.g Name name are different"
"3. Reserved cannot be use as variables"
"4. After first character we can use A-Z, a-z, underscore or digit "
"5. we cannot use special character e.g A%= 50"
"6. Multiple Assignment"
"7.swapping variables"
"8. deleting variables"
#
begining = "45"
start = 30 + 15
salary = 77
Begin = 45
print(begining)
print(Begin)
print(type(begining))
print(type(Begin))
print(id(begining))
print(id(Begin))
print(id(start))

a=10
b=5+5
c="10"
print(a,b,c)
print (type(a))
print (type(b))
print (type(c))
print (id(a))
print (id(b))
print (id(c))

import keyword
print(keyword.iskeyword("if"))
print(keyword.kwlist)
print("if".isidentifier())
IF=20
print(IF)

a_120 = 50
print(a_120)

name, salary, address, = "a", 45, "Noida"
print(name,salary,address)
print(name)
print(salary)

d = D = 80
print(d)
print(D)

name, salary = "a", 45
name, salary = salary, name
print(name, salary)

print(name)
del name
print(name)

"""
Importance of  underscore
1. Single Leading underscore (_*) // PRIVATE VARIABLES
 _a = 40 --> Private variable

2. Leading and Trailing Underscore (_*_) --> Magic methods 

3. Leading double underscore only (__*)
"""
print("abc".__len__())


