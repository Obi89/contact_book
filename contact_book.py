import csv

class Person(object):
    def __init__(self, vorname, nachname, adresse, telefon, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.adresse = adresse
        self.telefon = telefon
        self.alter = alter

    def ganzer_name(self):
        return self.vorname + " " + self.nachname
    def __str__(self):
        return "Name:" + self.ganzer_name() + "\nAdresse: " + str(self.adresse) + "\nTelefon: " + str(self.telefon) + "\nAlter: " + str(self.alter) + "\n------------"


def add_contact():
    print "Add new contact:"
    vorname = raw_input("Vorname:")
    nachname = raw_input("Nachname:")
    adresse = raw_input("Adresse:")
    telefon = raw_input("Telefon:")
    alter = raw_input("Alter:")
    new_contact = Person(vorname=vorname, nachname=nachname, adresse=adresse, telefon=telefon, alter=alter)
    contact_book.append(new_contact)
    print "New contact successfully added!"
    print "----------------------"

def show_contact():
    if not contact_book == []:
        for index, person in enumerate(contact_book):
            print "Nr.: " + str(index+1)
            print "Vorname: " + person.vorname
            print "Nachname: " + person.nachname
            print "Adresse: " + person.adresse
            print "Telefon: " + person.telefon
            print "Alter: " + person.alter
            print "----------------------"
    else:
        print "Contact book is empty, please add a contact!"

def search_contact():
    print "Who do you search?"
    search = raw_input("Type in the first name of the person:")

    for person in contact_book:
        if search == person.vorname:
            print "Vorname: " + person.vorname
            print "Nachname: " + person.nachname
            print "Adresse: " + person.adresse
            print "Telefon: " + person.telefon
            print "Alter: " + person.alter
            print "----------------------"
        else:
            next

    print 'Search end! If no result, no contact with this name! Type "5" and try it again!'


def edit_contact():
    print "\nSelect the number you like to edit!"
    for index, Person in enumerate(contact_book):
        print str(index + 1) + ") " + Person.ganzer_name()

    selected_nr = int(raw_input("Type the number from the contact you would edit:"))
    selected_nrint = int(selected_nr - 1)
    selected_contact = contact_book[selected_nrint]
    print "What would you like to edit at " + str(selected_contact.ganzer_name()) + "?"
    print "1.) Adresse?"
    print "2.) Telefon?"
    print "3.) Nachname?"
    what_edit = int(raw_input("What will you edit?"))
    if what_edit == 1:
        new_adresse = raw_input("Please enter a new address for " + str(selected_contact.ganzer_name()) + ":")
        selected_contact.adresse = new_adresse
        print "Adress of " + str(selected_contact.ganzer_name()) +  " successfully edit!"
        print "----------------------"
    elif what_edit == 2:
        new_telefon = raw_input("Please enter a new phone number for " + str(selected_contact.ganzer_name()) + ":")
        selected_contact.telefon = new_telefon
        print "Phone number of " + str(selected_contact.ganzer_name()) + " successfully edit!"
        print "----------------------"
    elif what_edit == 3:
        new_nachname = raw_input("Please enter a new last name for " + str(selected_contact.ganzer_name()) + ":")
        selected_contact.nachname = new_nachname
        print "Last name of " + str(selected_contact.ganzer_name()) +  " successfully edit!"
        print "----------------------"
    else:
        print "Edit canceled!"

def delete_contact():
    print "\nSelect the number you like to delete!"
    for index, Person in enumerate(contact_book):
        print str(index+1) + ") " + Person.ganzer_name()

    selected_nr = int(raw_input("Type the number from the contact you would delete:"))
    selected_nrint = int(selected_nr -1)
    selected_contact = contact_book[selected_nrint]
    print "Are you sure you would delete " + str(selected_contact.ganzer_name()) + "?"
    sure_delete = raw_input("yes/no")
    if sure_delete == "yes":
        contact_book.remove(selected_contact)
        print "Contact successfully delete!"
        print "----------------------"
    else:
        print "Delete canceled!"

def load_file():
    with open('contact_book.csv', "rb") as ofile:
        try:
            reader = csv.reader(ofile, delimiter=' ', quotechar='"')
            for person in reader:
                vorname = person[0]
                nachname = person[1]
                adresse = person[2]
                telefon = person[3]
                alter = person[4]
                new_contact = Person(vorname=vorname, nachname=nachname, adresse=adresse, telefon=telefon, alter=alter)
                contact_book.append(new_contact)
            print "Contacts complete loaded!"
        except:
            print "Not all contacts loaded!"




contact_book = []
load_file()
print "HELLO! I AM YOUR CONTACT BOOK!"
while True:
    print "\n1.) add a new contact"
    print "2.) show all contacts"
    print "3.) edit an existing contact"
    print "4.) delete a contact"
    print "5.) search a contact by name"
    print "6.) exit and save"
    choose = int(raw_input("Please choose a number (1/2/3/4/5/6)"))

    if choose == 1:
        add_contact()
    elif choose == 2:
        show_contact()
    elif choose == 3:
        edit_contact()
    elif choose == 4:
        delete_contact()
    elif choose == 5:
        search_contact()
    elif choose == 6:
        with open('contact_book.csv', "wb") as ifile:
            try:
                writer = csv.writer(ifile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)
                for person in contact_book:
                    ex_contact = (person.vorname, person.nachname, person.adresse, person.telefon, person.alter)
                    writer.writerow(ex_contact)

                print "\nContacts saved!"
                print "Thanks for using the contact book!"
                print "Goodbye!"
                break

            except:
                print "Error! Contacts NOT saved!"

    else:
        print "I don`t now what you want from me!"





