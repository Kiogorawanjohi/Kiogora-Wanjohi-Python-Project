#single line comment
"""
#multiline comment
#multiline comment
#multiline comment
#multiline commgient
#multiline comment
#multiline comment
#multiline comment
#multiline comment

#variables and different data types
student_name="Kiogora"#string
student_age="18"#integer
student_height="12.5"#float
is_male="true"#boolean

print("student name is:",student_name)
print("the students age is :",student_age)
print("student height is:",student_height)

firstname="Kiogora"
secondname="wanjohi"
fullname=firstname+" "+secondname
print(firstname+secondname)
#operators
#arithmetic operators
# + - * % ** //
print(5%2)
print(2%5)

student1="present"
student2="absent"
if student1=="present" or student2=="present":
    print("pass")
else:print("not pass")
print("hello world")
first,second,third,fourth="100","Isaac","Kiogora","Wanjohi"
print(third)
print(first+second+third+fourth)
y=10
print(int(first)+y)

print("type in the value of x:")
x=int(input())
if x%2==0:
    print("even")
else:
    print("odd")

print("which city are you from?")
city=str(input())
if city=="nairobi":
    print("you are eligible to be the president")
elif city=="kisumu":
    print("you are eligible to be the president")
elif city=="nakuru":
    print("you are eligible to be the presidentr")
elif city=="eldoret":
    print("you are eligible to be the president")
else:
    print("you are not eligible to be the president of kenya")



#a calculator
number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
operation=str(input("enter the operation"))
if operation=="add":
    print(number1+number2)
elif operation=="subtract":
    print(number1-number2)
elif operation=="divide":
    print(number1/number2)
elif operation=="multiply":
    print(number1*number2)

#defining my own function
def call(student):
    print("kindly come here:"+student)
#calling the function
call("Kiogora")

#tring to use python to determine the data type of input
odoz=input("provide an input to my program")
print(type(odoz))


#writing a program to add od  numbers
x=0
sum=0
while x<=10:
    if x%2==0:
       x=x+1
       continue
    else:sum=sum+x
    x=x+1
else:
    print(sum)"""

#program regarding visitors
visitors_number=0
ugandan=0
kenyan=0
count=0
print("hello i am Kiogora Wanjohi thankyou for choosing my visitors platform")
visitors_number=int(input("enter the total number of visitor"))
while visitors_number>count:
    country=input("which country are you from?")
    if country=="uganda":
        ugandans=ugandans+1
        count=count+1
    elif:country=="kenyan":
         kenyan=kenyan+1
         count=count+1
else:print("your country is not eligible for this service")
     print("the total number of ugandans is:"+ ugandans)
     print("the total number of kenyans is:"+ kenyans)
