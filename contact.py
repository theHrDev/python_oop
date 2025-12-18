# 13. Basic Contact Book
# 1. Add contact
# 2. View contact
# 3. Delete contact
# 4. View all contacts
# 5. Exit
class Contact:
    def __init__(self):
        self.contact_book =  {}       
        
    def add_contact(self,name,contact):
        
        if name not in self.contact_book:
            self.contact_book[name] = contact
            return f"{name} added successfully to the contact book"
        return "There is a contact with the existing name"
    
    def view_all_contact(self):
        if not self.contact_book:
            return "No contact in the contact book"
        
        return self.contact_book
    
    
    


def contact_book():
    contact = Contact()
    while(True):
        print("Pick a menu to get started")
        print("----- 1. Add contact ----")
        print("----- 2. Remove contact ----")
        print("----- 3. Edit contact -----")
        print("----- 4. View all contacts ----")
        print("----- 5. To exit ----")
        
        choice = input("\nEnter the menu: ")
        if choice == "1":
            name = input("Enter the name:")
            number = input(f"Enter the number of {name}:")
            print(contact.add_contact(name=name,contact=number))
        elif choice == "4":
            print(contact.view_all_contact())
        elif choice == "5":
            break
        else:
            print("Invalid input")
            

contact_book()