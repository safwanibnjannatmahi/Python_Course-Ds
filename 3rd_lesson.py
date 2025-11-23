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
""" import qrcode

img = qecode.make("")
img.save("name.png")
img.show()"""