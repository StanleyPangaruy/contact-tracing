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

#empty dictionary
contact = {}
while True:
    try:
        userInput = int(input("What do you want to do? (1-3) "))
        print("=================================")
        #adds an item to the dictionary
        if userInput == 1:
            print("Add a Contact")
            name = input("Full name: ")
            age = input("Age: ")
            address = input("Address: ")
            phoneNum = input("Phone number: ")
            mail = input("E-mail address: ")
            contactInfo = {
                "Name": name,
                "Age": age,
                "Address": address,
                "Phone number": phoneNum,
                "Email": mail
            }
            contact[name]=contactInfo
            print("Saved!")
            print("=================================")

        #searches an item in the dictionary
        elif userInput == 2:
            print("Search Contacts")
            fullname = input("Fullname: ")
            userAge = contact[fullname]["Age"]
            userAdd = contact[fullname]["Address"]
            userNum = contact[fullname]["Phone number"]
            userMail = contact[fullname]["Email"]
            print(f"""Age: {userAge}
Address: {userAdd}
Phone number: {userNum}
E-mail address: {userMail}
=================================""")

        #gives prompt for exitting the program
        elif userInput == 3:
            answer = input("Do you want to leave? (y/n) ")
            if answer == "y":
                break
            print("=================================")
        
        #gives prompt to input numbers from 1-3
        else:
            print("Choose from option 1-3")
            continue

    #gives prompt to enter the right type of data
    except ValueError:
        print("That is not an option.")
        print("=================================")






