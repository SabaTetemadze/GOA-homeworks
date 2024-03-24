#1) Write a program that takes an input from the user and checks if it's a positive, negative, or zero number using if-else

num = float(input("eneter number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")


#2)Write a program that prints all the even numbers between 1 and 20 using a for loop and if statement

for i in range(1,20 + 1):
    if i % 2 == 0:
        print(i)


#3)Write a program that calculates the sum of a number entered by the user using a while loop

number = int(input("enter number:"))

sum = 0
num0 = 0

while num0 <= number:
    sum = sum + num0
    num0 = num0 + 1

print(sum)


#4)Write a program that simulates a basic ATM. It should ask the user for their PIN,
#and if it's correct, display a text withdrawal, deposit, and balance

pincode = "1234"
user_input = input("enetr pincode:")

if user_input == pincode:
    print("bankis racxaebi")
else:
    print("nuh uh")



#5)Write a program that simulates a simple login system. Ask the user for a username and password,
#and if they enter "admin" and "password123", respectively, print "Login successful" using if-else

username = "admin"
password = "password123"

login0 = input("enter username:")
login1 = input("enter password:")
if username == login0 and password == login1:
    print("Login successful")
else:
    print("wrong username or password")


#6) Write a program that asks the user for their age and
#prints a message based on the age range (e.g., "Child", "Teenager", "Adult") using if-elif-else

age = int(input("enter your age:"))
if age <= 12:
    print("child")
elif age >= 20:
    print("adult")
else:
    print("teenager")