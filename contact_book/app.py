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

search_contacts()