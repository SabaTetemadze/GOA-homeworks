
authorized = False
password = "datka78"

while authorized != True:
    user_input = input("please enter password:")
    if user_input == password:
        print("Access granted")
        authorized = True