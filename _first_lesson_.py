##Q1. Create a function say_hello() that prints: "Hello, World!"
##Q2. Create a function square(num) that returns the square of a number.
##Q3. Write a function full_name(fname, lname) that prints the full name.
##Q4. Create a function add_three(a, b, c) that returns the sum of three numbers.
##Q5. Write a function area_circle(r) that returns area of circle. (Use 3.14)

def say_hello():
    print("hello, World!")

say_hello()


def square(num):
    return num * num


result = square(2)
print(result)

def full_name(fname,lname):
    print("Full name:", fname,lname)

full_name("Safwan","Mahi")

def add_three(a,b,c):
    return a+b+c
result=add_three(2,3,2)
print("The sum of three numbers",result)

def area_circle(r):
    return 3.1416*r*r
result= area_circle(20)
print("the circle area is:", result)
