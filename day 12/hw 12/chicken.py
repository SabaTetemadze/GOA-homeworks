#1)Calculate the sum of all even numbers from 1 to 10 using a while loop

number = 10
sum = 0
num = 0
while num <= number:
    sum = sum + num
    num = num + 2
print(sum)
print(" ")


#2)while ციკლის მეშვეობით შეამოწმეთ რიცხვები 1 დან 20 ჩათვლით, რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტეთ ეგ რიცხვი

number0 = 20
num0 = 1
while num0 <= number0:
    if num0 % 3==0 and num0 % 5 == 0:
        print(num0)
    num0 = num0 + 1
print(" ")


#3)for ციკლის მეშვეობით დაბეჭდეთ ყველა რიცხვი 1-100 ჩათვლით რომელიც იყოფა 5 ზე

for i in range(1,100 + 1):
    if i % 5 == 0:
        print(i)
print(" ")


#4) for ციკლის მეშვეობით დაბეწეთ ყველა ის ირცხვი რომელიც იყოფა 6_ზე 1 დან 20 ის ჩათვლით

for i in range(1,20):
    if i % 6 == 0:
        print(i)
