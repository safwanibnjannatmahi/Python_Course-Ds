#---------------------------For Loop Practice---------------------------#
numbers=[1,2,3,4,5,5,6]
for val in numbers:
    print(val)


numbers=[1,2,3,4,5,5,6]
for val in numbers:
    odd = val % 2 !=0
    if odd:
        print(val,end=""); print("The numbr is Odd")
    else:
        print(val, end=""); print("The number is Even ")

#-----------------------index number found not found------------------------
numbers=[1,2,3,4,5,5,6]
X=3
index=0

for num in numbers:
    if num == X:
        print("The number is Found:",index)
        break
    else:
        print("There is no number you emterd")
    index +=1
#---------------------range----------------------

for number in range (1,100):#here (start,end,step)
    print(number)
#print all the even number in bettwen 50-100 using loop
for number in range (50,100,2):#step is like 10 %2!=0 we dont have to write all this 
    print(number)

#for a to z 
for alphabet in range (ord("A"), ord("Z")+1):
    print(chr(alphabet))
for code in range (ord('a'),ord('z')+1):
    print(chr(code))
