#-------------------------oparetor___________________--------------------------------

## These are The arethmatic opparetor.

# + addition X +Y
# - subtraction X - Y
# * multiplication X * Y
# / division X / Y
# % modulus X % Y
# // floor division X // Y
# ** exponentiation X ** Y

##Assingment Oparetor 
# =
#  +=
# -=
# *=
# /=
# %=
# **=

num = 5
num += num  #( this Are called syntactic sugar iver the year in the industry)
print (num)


## Comparison Oparetor
# ==  Equal to
# !=  Not equal to
# >  Greater than
# <  Less than
# >=  Greater than or equal to
# <=  Less than or equal to

## Logical Oparetor
# and   
# or
# not

## Identity Oparetor
# is
# is not

X = 10 
Y = 5

print(X is Y)

print(X is not Y)


##membership Oparetor 
#in 
# not in

student = ["Mahi","safwan","maya"]
print("Janat" not in student)

##bitwise Oparetor 
# &  AND
# |  OR
# ^  XOR
# ~  NOT
# <<  Zero fill left shift
# >>  Signed right shift
a = 60    # 60 = 0011 1100
b = 13    # 13 = 0000 1101  
c = 0
c = a & b       # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)
c = a | b       # 61 = 0011 1101
print ("Line 2 - Value of c is ", c)
c = a ^ b       # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)
c = ~a        # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)
c = a << 2   # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)
c = a >> 2   # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
#--------------------------Datatype______----------------------------------------------

# Text -> String Data Type = str
#nemaric -> integer = int, decimal = float , complex = complex
#boolean -> True, False, 0, 1
#None -> none 

num = None
print(type(num))

def do_nothing():  #when we have ay variable who has no work or value python automatic take that to none
    pass 
print(do_nothing())
#_-------------------------string_________--------------------------
name="Safwan"

print(name[0:6])# in here python no need to run loop for print value in a range
print(name[:6])# in that case we can write this showing first to the range 
a = "Hello world"

print(a.upper())# for upper Alphabet
print(a.lower())
print(a.replace("world","Safwan")) #it well replace 1st to the second.
print(a.split(","))# it split the two text to separet memori

# String concatanation is Modifi two string one to another.

name = "Shihab"

age= 23

print(f"My name is {name} My age is {age}")#this is when we use variable in one line 


#-==================QR code================================================
"""import qrcode

img = qecode.make("")
img.save("name.png")
img.show() """

#===========================homework solution=============================
#1. Easy — Data Types Create three variables: ● an int ● a float ● a string Print each variable and also print their data types using type().

my_integer = 10
my_float = 3.14
my_string = "Hello Python"

print("Integer variable:", my_integer, "Type:", type(my_integer))
print("Float variable:", my_float, "Type:", type(my_float))
print("String variable:", my_string, "Type:", type(my_string))

"""   2. Easy — Arithmetic & Assignment Operators
Take two numbers from the user using input(). Perform the following operations and print the results:
● addition
● subtraction
● multiplication
● division
Then update the first number using += by 5 and print it. """

num1=int(input("enter the number 1 "))
num2=int(input("Enter the num2"))

addition= num1 + num2

subtraction= num1 - num2

multiplication= num1 * num2

divition= num1 / num2 

num1 += 5

print(f"updated num1 is {num1},\naddotion of two number is {addition}.\nsubtraction of two number is{subtraction},\nmultiplication of two number is {multiplication},\ndivition of two number is {divition}  ")

"""3.Easy — Comparison & Logical Operators
Write a program that checks:
● if a number is greater than 10
● AND less than 50
Print True or False using logical operator and.""" 
num=int(input("Enter the number:"))

print(num > 10 and num < 50 )


"""4. Easy — String Practice
Given the string:
text = " Hello Python World "
Do the following:
● remove extra spaces
● convert to uppercase
● replace "Python" with "AI" Print the final result."""  
text = " Hello Python World "

print(text.strip())   #strip() mainly use for remove extra space//
print(text.strip().upper())
print(text.strip().replace("Python","AI"))

"""Write a program that:
1. Takes a sentence from the user.
2. Check if the word "Python" is in the sentence.
Create an expression and evaluate it: 2 + 3 * 4 - 10 / 2
3.
4. Print the value of the expression and explain why the result is what it is (based on operator precedence)."""  


# 1. Takes a sentence from the user.
sentence = input("Enter a sentence: ")

# 2. Check if the word "Python" is in the sentence.
has_python = "Python" in sentence
print(f"Does the sentence contain 'Python'? {has_python}")

# 3. Create an expression and evaluate it: 2 + 3 * 4 - 10 / 2
expression_result = 2 + 3 * 4 - 10 / 2

# 4. Print the value of the expression and explain why the result is what it is (based on operator precedence).
print(f"The value of the expression (2 + 3 * 4 - 10 / 2) is: {expression_result}")
print("Explanation of the result based on operator precedence:")
print("1. Multiplication (3 * 4) is performed first: 12")
print("2. Division (10 / 2) is performed next: 5.0")
print("3. Addition (2 + 12) is performed: 14")
print("4. Subtraction (14 - 5.0) is performed last: 9.0")
