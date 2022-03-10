"""
Data Type
1. Numeric
Integer
Float
Complex
Integer can hold upto any length. limitation is availability of memory. happen in python 3.X
1. base 10 - decimal form
1. base 2 - binary form ( 0 to 1)
3. base 8 - Octal form (we use the number 0 to 7 base 8)
4. base 16 - Hexadecimal form (we use the number 0 to 15)
Float
A decimal no is called floating time no
A Floating value is accurate upto 15 decimal points only after that it round off the no.
Exponential Number 2e5 = 2*10^5 (same as 2 ** 5
"""

a, b, c = 7, 200000000004567890445683990404445678, 3.3
print(a, b, c)
print(type(a))
print(type(b))
print (type(c))

print ((1.1+3.3) == 4.4)
print ((1.1+2.2) == 3.3)
print (1/2,1/3)

import decimal
print(decimal.Decimal(0.3))

dec1, bin_2, oct1, hex1 = 23, 0B110, 0o145, 0X145
print(dec1, bin_2, oct1,hex1)
print(bin(dec1))
print(oct(dec1))
print(hex(dec1))
"""print(int(bin2)), print(int(oct1)), print(int(hex1)) , print(int(0b11)) not possible"""
# print(int(2+4j)) --> Conversion is not possible
print(int(5.9))

print(8e2)
print(8**2)
print(type(8e2))   #int
print(type(8**2))  #float

float1 = 5.11
print(isinstance(float1,float))
print(type(float1))

from math import pi
print(pi)

inf=float('Inf')
print(20000<inf)
print (type(inf))
print (id(inf))

# Treat it as an assignment, why it returned 2.2222222222222228
fl1 = 2.2222222222222229
fl2 = 1.1111111111111119
print(fl1)
print(fl2)

# 1.2 * 10^3 --> Scientific Notations / Exponential
# We can represent more significant values in lesser space
print(1.2e3)
print(15.68e10)

"""
How will you verify if the given data is integer ?
num = 7897987987987987
print(type(num))
print(isinstance(num, int))"""







