#Exercise 1: Profile Creator Create variables for a person's profile:
name = "Ndzi Jerry"
age = 44
hiegth = 1.78
is_Student =True
print(f"{name} {type(name)}")
print(f"{age} {type(age)}")
print(f"{hiegth} {type(hiegth)}")
print(f"{is_Student} {type(is_Student)}")

#Exercise 2: Type Challenge
#What are their types?
a = "10"  #string
b = 10    #integer
c = 10.0    #float

#Can you add a + b? Why/why not?
#Answer: No. a is a string and b is an integer.

#Can you add b + c? Why does it work?
#Answer: Yes. b is an integer and c is a float.

#Exercise 3: Conversion Read a user's age as string, convert to int, add 10 years, print result.
age  = "22"
age =int(age) + 10
print(age)

#Exercise 4: Text Processing 
text = " Hello, World! HELLO "
text = text.strip()
text = text.lower()
count = text.count("hello")
text = text.replace("world", "python")

#Exercise 5: Slicing Find the file extension of "document.pdf" using slicing.
fileName = "document.pdf"
dot =fileName.rfind('.')
extension = fileName[dot+1:]
print(f"extension: {extension}")

#Exercise 6: Email Validator Check if an email contains "@" and ends with ".com"

#Exercise 7: Calculator Read two numbers, perform +, -, *, / and print.
num1 =5
num2 =3
print(f"num1+num2 = {num1+num2}")
print(f"num1-num2 = {num1-num2}")
print(f"num1*num2 = {num1*num2}")
print(f"num1/num2 = {num1/num2}")

#Exercise 8: Temperature Convert 25 C to F using F = (C * 9/5) + 32
C = 25
F = (C*9/5)+32
print(f"F = {F}")

#Exercise 9: Percentage Calculate what percentage 25 is of 200.
percentage =(25/200)*100
print(f"{percentage} %")