contact_book = [
    {
        "name": "Rahi",
        "phone":"0150000000",
        "email": "rahi@example.com"
    },
    {
        "name": "Ebrahim",
        "phone":"0160000000",
        "email": "rahi@example.com"
    },
    {
        "name": "Rahi",
        "phone":"0170000000",
        "email": "tuhin@example.com"
    }
]



def create_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact_book.append(contact)
    print("Contact created successfully")


def view_all_contacts():
    for contact in contact_book:
        print(
            contact["name"],
            contact["phone"],
            contact["email"],
            sep=" | ",
        )


def search_contacts():
    search_term = input("Enter what you want to search: ")
    for contact in contact_book:
        if search_term.lower() in contact['name'].lower(): 
            print(f"Found: {contact['name']} - {contact['phone']}")


def remove_contact():
    search_term = input("Enter what you want to search: ")
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact['name'].lower(): 
            print(f"{index+1}. Found: {contact['name']} - {contact['phone']}")

    selected_index = input("Enter an index to remove: ")
    selected_index = int(selected_index)

    contact_book.pop(selected_index - 1)



def update_contact():
    # 1. select the contact
    found_search_result = False
    search_term = input("Enter text to search to update: ")
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact['name'].lower():
            found_search_result= True
            print(f"{index+1}. {contact['name']} - {contact['phone']} ")

    if not found_search_result:
        print("No item found")
        return
    
    selected_index = input("Enter an contact to update: ")
    selected_index = int(selected_index)

    # 2. get the new values
    new_name = input("Enter new Name: ")
    new_phone = input("Enter new phone: ")
    new_email = input("Enter new email: ")

    # 3. Replace old values with new values
    # method 1
    # contact_book[selected_index-1]['name'] = new_name
    # contact_book[selected_index-1]['phone'] = new_phone
    # contact_book[selected_index-1]['email'] = new_email

    # method 2
    contact_book[selected_index-1].update(
        {
            'name':new_name,
            'phone':new_phone,
            'email': new_email
        }
    )






print("Welkcome!")
menu_text = """
Your Options:
1. Create Contact
2. View All Contacts
3. Search Contacts
4. Remove Contact
5. Update Contact
0. Exit
"""
while(True):
    print(menu_text)
    choice = input ("Enter Your Choice: ")

    if choice == "1":
        create_contact()
    elif choice == "2":
        view_all_contacts()
    elif choice == "3":
        search_contacts()
    elif choice =="4":
        remove_contact()
    elif choice == "5":
        update_contact()
    elif choice == "0":
        print("Thank You!")
        break
    else:
        print("Wrong Choice")