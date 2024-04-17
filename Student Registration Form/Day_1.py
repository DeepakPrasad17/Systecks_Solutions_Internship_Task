'''

#String Concatenation

first_name ='Tony'
last_name = "Stark"
age = 51
is_genius = True
print(first_name +" "+  last_name + " of " + str(age )+ " years old " + str(is_genius))

old_age = input('Enter your age :- ')
new_age = int(old_age) + 2
print(new_age)

num1=int(input("Enter number 1 :- "))
num2=int(input("Enter number 2 :- "))
sum = num1+num2
print(sum)

# Variable Conversion
name = "deepak Prasad is the best businessman of the world "
print(name.find('P'))
print(name.replace('Prasad','Buisnessman'))
print(name.split())
print(name.capitalize())
print(name.center(60))
print(name.count("b"))
print(name.endswith("!!!"))
print(len(name))

i=5
i+=2
i-=2
print(i)

# Arithematic Operator
num1=int(input("Enter first number :- "))
operator = input("Enter operator {+,- ,*,/} :- ")
num2=int(input("Enter second number :- "))

if operator =="+":
    print(num1+num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print('Invalid Operator')

# Range

num = range(5)
print(num)

# While Loop

i=1
while i<=5:
    print(i*"*")
    i=i+1

# For Loop
for i in range(10):
    print(i+1)

marks = [95 ,96,97]
print(marks[1]) # To print the particular marks out of the list.
print(marks[0:2]) # To print the marks from range 0 to 2

for score in marks:
    print(score)

marks.append(99) # To add the element in the end of the list
print(marks)

marks.insert(2,100)# To insert the new element in te list
print(marks)

print(64 in marks) #To check the number present in the list True or False

marks =[95,96,97,98]
i=0
while i<len(marks):
    print(marks[i])
    i=i+1

marks.clear() # Clear function used to clear the list
print(marks)

# Keywords

# break statement
students = ["ram","shyam","kishan","radha","radhika"]
for student in students :
    if student == "radha":
        break;
    print(student)

# continue statement
students = ["ram","shyam","kishan","radha","radhika"]
for student in students :
    if student == "kishan":
        continue;
    print(student)

# Tuple
marks = (95,96,97) # tuple is the list which cannot be changed after creating
print(marks.count(96))
print(marks.index(97))

# Set
marks ={95,98,97,97,97} # Only stores unique values and no index exists in sets
print(marks)
for score in marks :
    print(score)

# Dictonary

marks ={"Maths":99 , "Chemistry":98 , "English":97}  # Stored with key and value form
print(marks["English"])
marks["Physics"]=100;
print(marks)
marks["Maths"]=100;
print(marks) '''

# Functions
import math
from math import factorial
print(dir(math))
print(factorial(5))

def deepak():
    print("xyz")
deepak()



















































