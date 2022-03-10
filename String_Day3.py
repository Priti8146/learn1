# STRINGS - Sequence of characters

# Ashish

name = 'Ashish'
print(name[0])
print (name[1])

# name2 = "Priti'         syntax error and should be priority
# print(name2[100])       # string out of range


"""
My name is "Ashish" ..........print
Will throw syntax error print ("My name is "Ashish"") 
"""
print ('My name is "Ashish"')

print(""" 
My name is "ashish"
""")  # triple quotation will print exactly in same way. complete white board
print ( "my name is \"Abbas\"")    #\ will consider as regular character.This is called as escape sequence

# triple quotation will print exactly in same way. complete white board
print("""         
##############
###########
""")

print(
"my"\
" name"\
" is"\
" Priti"\
) # my name is Priti

print("my\nname\nis\nPriti") # my name is Priti in different line

"""
 0   1   2   3   4   5   6   7
 B   I   S   W   A   J   I   T
-8  -7  -6  -5  -4  -3  -2  -1 
"""
name5 = "BISWAJIT"
print (name5[2])
print (name5[-5])
# print (name5[8]) out of range
# print (name5[-9]) out of range
print (name5[+6])
# print (name5[+8]) out of range

"""
 0   1   2   3   4   5   6   7   8   9
 A   B   C   D   E   F   G   H   I   J
-10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
positive slicing
[begin : end : step]
[start : (length-1) : step size]
By default 
begin is 0  (can be out of range value)
end is length of string (which is 10)
step size is 1
negative slicing
begin : end : step
-1 : end-1 : step will bee negative
"""
alpha="ABCDEFGHIJ"
print(alpha[1:5])    #BCDE
print(alpha[1:5:1])  #BCDE
print(alpha[1:5:2])  #BD
print(alpha[1:7:3])  #BE
print(alpha[::1])    #ABCDEFGHIJ
print(len(alpha))    #10   ~~~length of string 10 index is 9
print (alpha[:2:])   #AB
## print(aplha[::0]) error
print(alpha[7:4:-1])    # HGF
# print (alpha[3,7,-1])  nothing to print
print(alpha[-4:1:-1])   # GFEDC
print(alpha[-4:1:-2])   # GEC
print(alpha[-4:1:-1])   # GFEDC
# print(alpha[0:-11:1])   nothing to print
print(alpha[0:-11:-1])
print(alpha[0:-11:1])   # nothing to print
print(alpha[-5:-9:-2])  # FD
print(alpha[10000:3:-1])  #JIHGFE

"""
input is a function we take input from user
every thing in input function is string

string formatter
    1. format method - format is used under the print function - 
    2. % Operator 
                %d --> Integers
                %s --> Strings
                %f --> Float
    3. f-Strings

E.g

sal = "870"
print(sal)
print(type(sal))
a=[1,2,3,4,5,5]
print("Salary is %s and address is %s" %(sal, sal))
print("My Salary is Rs. {0} and name is {1}".format(sal, "Ashish"))
print("Welcome to {0}".format(a))
print(f"My name is {a} and Salary is {sal}")

a= [1,2,23,3,]
sal= int(input("enter salary "))
print(f"My name is {a} and Salary is {sal}")
print(type(a))
print(type(sal))

sal= input("enter salary is ")
print(f"{sal}")

sal= int(input("enter salary is "))
print(f"{sal}")

sal= float(input("enter salary is "))
print(f"{sal}")

sal= str(input("enter salary is "))
print(f"{sal}")

a=input("")
b=input("")
c=a/b         # by default it is string hence cannot be divided
print(f"{c}")


a=int(input(""))
b=int(input(""))
c=a/b         # if entered 0/0 then error will come
print(f"{c}")


a=float(input(""))
b=float(input(""))
c=a/b        
print(f"{c}")

a=int(input(""))
b=int(input(""))
c=a/b        
print(f"{c}")

a=int(input(""))
b=int(input(""))
c=int(a/b)         #
print(f"{c}")

# print("10"+10)  cannot concatenate string and integer

print("10"+"10")
print(10+10)
print(type("10"),type(10))

"""#
#function
string1 = "    Way2  Automation      "
mul =78
digit="77"
print(len(string1))
print(str(78), type(str(mul)))
print(string1.lower())
print(string1.upper())
print(string1.strip())
print(digit.isdigit())
print(digit.isalnum())
print(digit.isalpha())
"""
# string operation

     1. Identity Operation (is and is not)
     how will you verify Ashish = ashish is not same
     
     2. Membership Operation (in and not in)
"""

a= "Ashish"
b= "ashish"
print(a==b)
print(a.__eq__(b))
print("Ashish" is "ashish")
print("Ashish" is "Ashish")
print("Ashish" is not "Ashish")

#pp is in apple
c='apple'
print("pp" in "apple")
print("pp" not in "apple")

















