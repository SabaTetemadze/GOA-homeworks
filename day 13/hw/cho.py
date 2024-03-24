# 1)Write a program that prints numbers from 1 to 10 using a while loop

number = 10
num = 1
while num <= number:
    print(num)
    num = num + 1

# 2)Write a program that prints the even numbers from 1 to 10 using a for loop

for i in range(1,10 + 1):
    print(i)


#3)Write a program that asks the user to enter a number and then prints whether the number is positive, negative, or zero using an if-else statement

i = input("enter number:")
if i < 0:
    print("Negative")
elif i > 0:
    print("Positive")
else:
    print("Zero")


#4)Write a program that asks the user to enter a password. If the password is "abc123", print "Access granted";
#otherwise, print "Access denied"

password = "abc123"
user_password = input("enter password:")
if user_password == password:
    print("access granted!")
else:
    print("nuh uh")


#5)Write a program that prints numbers from 1 to 10, but stops if the number is 5 using a while loop and the break statement

numb = 10
sus = 1
while sus <= numb:
    print(sus)
    if sus == 5 - 1:
        break
    sus = sus + 1


#6)Write a program that asks the user to enter a number between 1 and 5. If the number is less than 1 or greater than 5, print "Invalid input".
#If the number is between 1 and 5, print "Valid input"
    
number = int(input("enter number between 1 and 5:"))
if number <= 5 and number >0:
    print("valid input")
else:
    print("invalid input")


#7)Write a program that asks the user to enter a number. If the number is divisible by 3, print "Fizz". If the number is divisible by 5,
# print "Buzz". If the number is divisible by both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.
    
ii = int(input("enter number:"))
if ii % 3 == 0 and ii % 5 == 0:
    print("FizzBuzz")
elif ii % 5 == 0:
    print("Buzz")
elif ii % 3 == 0:
    print("Fizz")
else:
    print(ii)