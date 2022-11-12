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
    try:
        userInput = int(input("What do you want to do? "))
        print("=================================")
        if userInput == 1:
            print("Add a Contact")
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
            print("=================================")

        elif userInput == 2:
            print("Search Contacts")
            fullname = input("Fullname: ")
            userAge = contact[fullname]["Age"]
            userAdd = contact[fullname]["Address"]
            userNum = contact[fullname]["Phone number"]
            print(f"""Age: {userAge}
Address: {userAdd}
Phone number: {userNum}
=================================""")

        elif userInput == 3:
            answer = input("Do you want to leave? (y/n) ")
            if answer == "y":
                break
            print("=================================")
        
        else:
            print("Choose from option 1-3")
            continue
    except ValueError:
        print("That is not an option.")
        print("=================================")






#perform the selected option