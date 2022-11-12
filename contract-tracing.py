#Contact Tracing

#create and display a menu of options
print("""
=======CONTACT TRACING APP=======

    Menu:
        1 -> Add an item
        2 -> Search
        3 -> Exit (y/n)

=================================""")

#ask for an input from the user to choose from the options

contact = {}
while True:
    userInput = int(input("What do you want to do? "))
    if userInput == 1:
        name = input("Full name: ")
        age = input("Age: ")
        address = input("Address: ")
        phoneNum = input("Phone number: ")
        contactInfo = {
            "Name": name,
            "Age": age,
            "Address": address,
            "Phone number": phoneNum
        }
        contact[name]=contactInfo
        print("Saved!")

    if userInput == 2:
        fullname = input("Fullname: ")
        x = contact[fullname]
        for keys,value in x:
            print(keys,value)


    if userInput == 3:
        answer = input("Exit? ")
        if answer == "y":
            break


#perform the selected option

# contact = {}
# while True:
#     name = input("Full name: ")
#     age = input("Age: ")
#     address = input("Address: ")
#     phoneNum = input("Phone number: ")

#     contactInfo = {
#         "Name": name,
#         "Age": age,
#         "Address": address,
#         "Phone number": phoneNum
#     }

#     contact[name]=contactInfo
#     print(contact)

    # contact[name] = contactInfo
    # print(contact)







# userInput = int(input("What do you want to do? "))
# if userInput == 1:
#     name = input("Full name: ")
#     age = input("Age: ")
#     address = input("Address: ")
#     phoneNum = input("Phone number: ")
#     contactInfo = {
#         "Name": name,
#         "Age": age,
#         "Address": address,
#         "Phone number": phoneNum
#     }
#     print(contactInfo)  






#perform the selected option