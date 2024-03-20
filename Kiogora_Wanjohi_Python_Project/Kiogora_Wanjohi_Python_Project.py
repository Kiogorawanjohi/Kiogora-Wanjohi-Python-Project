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
    print(sum)

#program regarding visitors
visitors_number=0
ugandans=0
kenyans=0
count=0
print("hello i am Kiogora Wanjohi thankyou for choosing my visitors platform")
visitors_number=int(input("enter the total number of visitor"))
while visitors_number>count:
    country=input("which country are you from?")
    if country.lower()=="uganda":
        ugandans=ugandans+1
        count=count+1
    elif country.lower()=="kenya":
        kenyans=kenyans+1
        count=count+1
print("the total number of ugandans is:"+ str(ugandans))
print("the total number of kenyans is:"+ str(kenyans))

#defining my function to add odd and even numbers
def odd_add_check(first,last):
    sum = 0
    for number in range(first,last+1):
        if number%2==0:
            continue
        else:sum+=number
    return sum

result=odd_add_check(2,34)
print(result)

#sum of all even numbers between 1 and 10
sum=0
for number in range(1,11):
    if number%2==0:
        sum+=number

print(sum)

#creating and modifying lists
details=["Jack","Isaac","Kiogora","wanjohi",13790]
print(details)
details.append("Nyeri high school")
print(details)
details.extend([4,5])
print(details)

#tasking to enter names of students in a list and print out
names=[]
student1=input("student1 kindly enter your name")
print("you have entered the name",student1)
names.append(student1)
student2=input("student2 kindly enter your name")
print("you have entered the name",student2)
names.append(student2)
student3=input("student3 kindly enter your name")
print("you have entered the name",student3)
names.append(student3)
print(names)

names=[]
totalnumber=int(input("enter the number of names you want to enter"))
for name in range(totalnumber+1):
    names.append(input(name))
    print("you have entered the name",name)


    print(name)

#task involving the application of tuples dictionaries and set
#dict containing student name and the grades in maths bio and chem respectively
dict={}
dict={"jack":(20,30,40),"joe":(20,50,60),"isaac":(20,70,80),"kiogora":(20,90,100),"wanjohi":(20,100,200)}
#task to be continued

import numbers

#program that finds the largest number in a list using parametised functions
list_of_numbers=(input("enter a list of numbers seperated by commas"))
list_of_numbers=[int(num) for num in list_of_numbers.split(",")]
def checking_largest_number(list):
    biggest_number = list[0]
    if len(list) == 0:
        print("no numbers entered")
        biggest_number="invalid"
    else:
        for number in list:
            if number>biggest_number:
                biggest_number=number
    return biggest_number
largest=checking_largest_number(list_of_numbers)
print(largest)

#write a program that outputs the repeated elements in a list
repeated_elements=[]
count={}
list=(input("enter a list of elements seperated by commas"))
list=[elements.lower() for elements in list.split(",")]
for element in list:
    if element in count.keys():
        count[element]+=1
    else:count[element]=1
for element,number in count.items():
    if number>1:
        repeated_elements.append(element)

print(repeated_elements)

#program that counts easily
numbers=[1,2,3,4,5,3,2,4,5]
x=numbers.count(1)
print(x)
#program that adds to a tuple
empty_tuple = (input("enter values in this tuple"))
print(empty_tuple)
adding_tuple = (input("enter the values you would like to add to your tuple"))
new_tuple=empty_tuple+adding_tuple
print(new_tuple)
"""





#using tuples write a program that adds an item to a list
#using dicyionaries write a program that deletes a list of keys from a dictionary
#using dictionaries write a program that checks if a valque exists in a dictionary
#using dictionaries write a program that converts two lists into a dictionary
#using sets write a program that adds items to a list
#using sets write a program that removes items from a list





