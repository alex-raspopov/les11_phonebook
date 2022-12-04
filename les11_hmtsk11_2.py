# Task 2 - Extend Phonebook application
# Functionality of Phonebook application:
# (1) Add new entries
# (2) Search:
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# (3) Delete a record for a given telephone number
# (4) Update a record for a given telephone number
# (5) An option to exit the program
# (6) The first argument to the application should be the name of the phonebook.
# (7) Application should load JSON data, if it is present in the folder with application, else raise an error.
# (8) After the user exits, all data should be saved to loaded JSON.

import sys


def add():  # (1)
    print('\n>> Enter contact details')
    dic = {}
    for i in ['Name', 'Last name', 'Number', 'City']:
        dic[i] = input(f'{i}: ')
    print('>>> New contact added\n')
    return dic


def search():  # (2)
    srch = input('\n>> Search contact by: ').lower()
    i = -1
    for entry in db:
        i += 1
        if srch in entry['Number']\
                or srch in entry['Name'].lower()\
                or srch in entry['Last name'].lower()\
                or srch in entry['City'].lower()\
                or srch.split()[0] in entry['Name'].lower()\
                or srch.split()[0] in entry['Last name'].lower():
            print(entry)
    print('>>> Exit search menu\n')


def delete():  # (3)
    search_number = input('\n>> Delete contact by number: ')
    i = -1
    while i + len(db) < len(db):
        for entry in db:
            i += 1
            if search_number in entry['Number']:
                print(entry)
                if input('Delete contact? [Y] to continue, else to skip: ').lower() == 'y':
                    db.pop(i)
                    print('>>> Contact deleted\n')
                else:
                    print('>>> Contact delete skipped\n')
    print('>>> Exit delete menu\n')


def update():  # (4)
    search_number = input('\n>> Update contact by number: ')
    i = -1
    while i + len(db) < len(db):
        for entry in db:
            i += 1
            if search_number in entry['Number']:
                print(entry)
                if input('Update contact? [Y] to continue, else to skip: ').lower() == 'y':
                    db[i] = add()
                    print('>>> Contact updated\n')
                else:
                    print('>>> Contact update skipped\n')
    print('>>> Exit update menu\n')


def display():  # (optional)
    _ = '- '*40
    print(_)
    for entry in db:
        print(entry)
    print(_+'\n')


def phonebook(name):  # (6)
    import json
    global db
    try:
        with open(f'{name}', 'r') as file:
            db = json.load(file)
            print('Database successfully loaded. Chose option to continue')
    except FileNotFoundError:  # (7)
        if input('Phonebook not found. Any key to create new or [E] to exit: ').lower() == 'e':
            sys.exit("Sometimes it's better stop before you get too far. Goodbye!")
        else:
            print('Phonebook is empty')
            db = [add()]
    while True:
        with open(f'{name}', 'w') as file:  # (8)
            json.dump(db, file, indent=4)
        to_do = input('> [A]dd, [S]earch, [D]elete, [U]pdate, [P]rint, [E]xit: ').lower()
        if to_do == 'a':  # (1)
            db.append(add())
        elif to_do == 's':  # (2)
            search()
        elif to_do == 'd':  # (3)
            delete()
        elif to_do == 'u':  # (4)
            update()
        elif to_do == 'p':  # (optional)
            display()
        elif to_do == 'e':  # (5)
            break


##########################################################
try:
    phonebook(sys.argv[1])  # (6)
except IndexError:
    name = input('Phonebook name not passed. Enter manually or [E] to exit: ')+'.json'
    while name == '.json':
        name = input('Enter name or [E] to exit: ') + '.json'
    if name[0].lower() == 'e':
        sys.exit('Come back with argument and call me, maybe')
    else:
        phonebook(name)
