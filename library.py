class Library:
    def __init__(self):
        self.books = {}
        
    def add_books(self,author,book):
        self.books[author] = book
        return "Successfully added"
    
    def list_books(self):
        return self.books
        
        
def librarian_action():
    librarian = Library()
    

    while(True):
        print("\n--- Library Menu ---")
        print("1. Add Books")
        print("2. List Books")
        choice = input("Choose an option (1-2): ")
    
        if choice == "1":
            book = input("Enter the name of the book: ")
            author = input("Enter the book author: ")
            print(librarian.add_books(book=book,author=author))
        if choice == "2":
            print(librarian.list_books())
            
        break
            
  
    

librarian_action()