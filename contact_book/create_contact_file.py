def create_contact(contact_book):
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

    with open('contacts.csv','a') as fp:
        new_contact = f"{contact['name']}, {contact['phone']}, {contact['email']}"
        fp.write(new_contact)
    
    return contact_book
