contacts = {}

def add_contact():
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    email = input('Enter your email: ')

    contacts[name] = {'name': name, 'phone': phone, 'email': email}

    print('Contact Added Successfully')

def view_contacts():
    if not contacts:
        print('No Contacts Found')
        return

    for name, info in contacts.items():
        print(f'Name: {name}')
        print(f'Phone: {info["phone"]}')
        print(f'Email: {info["email"]}')

def search_contacts():
    name = input('Enter name to search: ')

    if name in contacts:
        print('Contact found: ')
        print(f'Phone: {contacts[name]["phone"]}')
        print(f'Email: {contacts[name]["email"]}')
    else:
        print('No Contacts Found')

def delete_contact():
    name = input('Enter contact name to delete: ')
    if name in contacts:
        contacts.pop(name)
        print('Contact Deleted Successfully')
    else:
        print('No Contacts Found')

while True:
    print('Contact Manager')
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contacts')
    print('4. Delete Contact')
    print('5. Exit')

    choice = int(input('Enter your choice please: '))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contacts()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        print('Goodbye, thank you for using this program! ')
        break
    else:
        print('Invalid Choice')
