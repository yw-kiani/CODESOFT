#Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts[name] = contact
    print("Contact added successfully!")

# Function to view the contact list
def view_contacts():
    for idx, (name, contact) in enumerate(contacts.items(), start=1):
        print(f"{idx}. {name} - {contact['phone']}")

# Function to search for a contact
def search_contact():
    query = input("Enter the name or phone number to search: ")
    found = False
    for name, contact in contacts.items():
        if query in name or query in contact['phone']:
            print(f"Contact found: {name} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Contact found. Update the details:")
        contacts[name]['phone'] = input("New phone number: ")
        contacts[name]['email'] = input("New email: ")
        contacts[name]['address'] = input("New address: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu loop
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")