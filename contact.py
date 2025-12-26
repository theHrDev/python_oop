# 13. Basic Contact Book
# 1. Add contact
# 2. View contact
# 3. Delete contact
# 4. View all contacts
# 5. Exit
# Edit

import random;
class ContactBook:
    def __init__(self):
        self.contact_book =  {}       
        
    def add_contact(self,name,contact):
        
        if name not in self.contact_book:
            id = random.randint(10**2,10**3+1)
            new_contact = {"name":name,"contact":contact,"id":id}
            self.contact_book[id] = new_contact
            return f"{name} added successfully to the contact book"
        return "There is a contact with the existing name"
    
    def remove_contact(self,id):
        if id not in self.contact_book:
            return "Invalid ID"
        del_num = self.contact_book[id]
        print(del_num)
        del self.contact_book[id]
        return f"Contact deleted successfully"
    
    def view_single_contact(self,id):
        if id not in self.contact_book:
            return "No contact with the provided id"
        contact_detail = self.contact_book[id]
        return f"The details are {contact_detail}"
    
    def view_all_contact(self):
        if not self.contact_book:
            return "No contact in the contact book"
        
        return self.contact_book
    
    def edit(self,id,title,value):
        if not self.contact_book[id]:
            return "contact with the given id does not exist"
        
        selected_contact = self.contact_book[id]
        if not selected_contact[title]:
            return "No key with the name given"
        selected_contact[title] = value
        return "Successflly edited"
    
    


def contact_book():
    contact = ContactBook()
    while(True):
        print("Pick a menu to get started")
        print("----- 1. Add contact ----")
        print("----- 2. Remove contact ----")
        print("----- 3. Edit contact -----")
        print("----- 4. View single contact ----")
        print("----- 5. View all contacts ----")
        print("----- 6. To exit ----")
        
        choice = input("\nEnter the menu: ")
        if choice == "1":
            name = input("Enter the name: ")
            number = input(f"Enter the number of {name}: ")
            # if name or number == "":
            #     print("Enter a valid value")
            # else:
            print(contact.add_contact(name=name,contact=number))
        elif choice == "2":
            id = int(input("Enter the id for the contact to be deleted: "))
            print(contact.remove_contact(id))
        elif choice == "3":
            id = int(input("Enter the id for the contact to be view: "))
            title = input("Enter the key you want to edit: ")
            value = input("Enter the value for the key: ")
            print(contact.edit(id=id,value=value,title=title))
        elif choice == "4":
            id = int(input("Enter the id for the contact to be view: "))
            print(contact.view_single_contact(id=id))
        elif choice == "5":
            print(contact.view_all_contact())
        elif choice == "6":
            print("bye")
            break
        else:
            print("Invalid input")
            

contact_book()