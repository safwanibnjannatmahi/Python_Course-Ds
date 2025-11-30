isRaining= False  #it must have to take boolinan value.

if isRaining:
    print("Take umbrella ")

else:
    print("Dont Take umbrella")


print("Program Complited")


age=int(input("Enter your age"))

if age>= 18:
    print("You are eligble to vote")
else:
    print("Not eligble to vote ")

marks=int(input("Enter your marks:"))
if marks>100 or marks< 0:
    print("invalid Marks")
elif marks>= 90 and marks<=100:   # in python we have to use (elif) instate of (else if).
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("A-")
else:
    print("F")


yourage=int(input("Enter your age:"))

if yourage >=18:
    has_id= input("do you have your id (yes/no):")
    if has_id=="yes":
            print("you can  enter")
    else:
        print("You Cannot enter")

else:
    print("You are under age Go and drink Milk.")     

num=int(input("Enter a number:"))

if num > 0:
    print("positive")
elif num== 0:
    print("zero")
else: 
    print("Negetive")











    