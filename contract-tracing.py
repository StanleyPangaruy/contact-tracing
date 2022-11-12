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
while True:
    contactInfo = {}
    name = input("Full name: ")
    age = input("Age: ")
    address = input("Address: ")
    phoneNum = input("Phone number: ")

    contactInf = {
        "Name": name,
        "Age": age,
        "Address": address,
        "Phone number": phoneNum
    }

    contactInfo[name] = contactInf
    deets = contactInfo
    contactInfo.update(deets)
    print(contactInfo)



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