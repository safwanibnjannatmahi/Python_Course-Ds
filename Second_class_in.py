##vs code is a ide. as also some other ide's are there like pycharm ,spyder etc.This is like a translation of code into machine language.


##the perpous of print is to print something on the screen.
## consol == terminal
##if needed we  use end="" we can print second line in a same line. 
print("Hello, This is the first program i running to know print ", end=""); print("Hlw")
print("Hi!") 
##we have to use a single ''or "" for print.(must) just not for only print it is for all english word (string)
print('Comma'); print("Duble")
## for any number not need to use cotation "".
print(123)

##we dont need to use Cotation "" when ever we use Any (variable)
num=321
print(num)

## (Type) is used ofr seeing what is the datatype this is.
num=25 #intejer
num2=34.2 #float
num3="Safwan" #char or string
booleanVal= True #boolean

print(type(num))
print(type(num2))
print(type(num3))
print(type(booleanVal))

## assingment oparetor 
#=  +=  -=  *=  /=  //=  **=  %=
#oparetor we can use anything on the varuable like sum but no need to write sum i can take anything like sum.
num1=10
num2=5

sum = num1 - num2

print(sum) 

#for input from the keyboard // also when we have to input from keyboard the have to use datatype for numbers otherwise python take it as a string.
name=input("Enter your name:")

print("Hi ",name)

num1=int (input ("Enter number:"))
num2=int (input ("enter number"))
sum=num1+num2
print(sum)

##write a program to sum 2 number num1 and num2 ,
#  take it thoese number as user input and print the sum and its type

num1=int(input("enter a number"))
num2=int(input("enter a numer"))

print("sum is:" , num1 + num2)
print(type(num1 + num2))



#=====================================home work=============================================
"""  1. Write a program that takes two numbers from the user and prints their sum. (Easy)
2. Write a program to take a user’s name and age and print: ( Medium) "Hello [name], you are [age] years old!"
3. Create three variables (a, b, c) and print their average. (Easy)
4. Convert a float number (e.g., 5.9) into an integer using type casting and print both values. (easy)
5. Use operators to check if a number entered by the user is greater than 10 and print the result (True/False). (Hard)"""

#1 
num1=int(input("Enter the value of Number 1:"))
num2=int(input("Enter the value of number 2:"))

sum = num1 + num2

print("The Sum of this two number is:",sum)

#2
name=input("Enter Your name:")
age=int(input("enter your age:"))

print(f"Hello {name},You are {age} old")

#3
First_Number=int(input("Enter the first number:"))
Second_Number=int(input("Enter the seconf number:"))
Third_Number=int(input("Enter the third Number:"))

Avarage= (First_Number + Second_Number + Third_Number)/ 3

print("The avarage Number is ",Avarage)

#4
X= 5.7
y=int(X)
z=float(y)

print(f"The value of float was{X},Now the value of x in intizer is {y} ")

#5
number=int(input("enter a number that greter then 10:"))
print(number > 10)
