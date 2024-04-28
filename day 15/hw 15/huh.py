a = int(input("enter number:"))
if a % 2 == 0:
    print(str(a) + " is even")
else:
    print(a + 1)



parol = "GOA best"
log_in = False
while log_in == False:
    user = input("enter password: ")
    if user == parol:
        print("ok")
        log_in = True



m = [input("enter rame: ")]
if m[0] == "G" or "g":
    print(m)
else:
    print("gaajvi")


name0 = input("enter name: ") 
name1 = input("enter name: ")
name2 = input("enter name: ")
name3 = input("enter name: ")
name4 = input("enter name: ")

names = [name0, name1, name2, name3, name4]
print(names[:3])


num = 10
while num >= 0:
    print(num)
    num = num - 1



numi = int(input("enter number: "))
for i in range(2, numi, 2):
    print(i)