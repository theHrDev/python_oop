class Library:
    def __init__(self,book,author,books):
        self.book = book
        self.author = author
        self.books = books
        
    def add_books(self):
        self.books[self.author] = self.book
        return "Successfully added"
    
    def list_books(self):
        return self.books
        
        
def librarian_action():
    
    book = input("Enter the name of the book: ")
    author = input("Enter the book author: ")
    
    librarian = Library(book=book,author=author,books={})
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Books")
        print("2. List Books")
        # print("3. Check Balance")
        print("3. Exit")

        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            print(librarian.add_books())
        if choice == "2":
            print(librarian.list_books())
        if choice == "3":
            break

librarian_action()