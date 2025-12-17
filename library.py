class Library:
    def __init__(self):
        self.books = {}
        
    def add_books(self,author,book):
        if author not in self.books:
            self.books[author] = []
        self.books[author].append(book)
        return "Book added successfully"
    
    def list_books(self):
        if not self.books:
            return "No books found in the library"
        
        result = []

        for author,books in self.books.items():
            for book in books:
                result.append(f"{book} by {author}")
        return "\n".join(result)
        
    def remove_book(self,author,index):
        if author not in self.books():
            return "No book with the mentioned author"
        
        for books in author:
            if books[index]:
                books[index].remove()
                return "Book removed successfully"
                
            
        
def librarian_action():
    librarian = Library()
    

    while(True):
        print("\n--- Library Menu ---")
        print("1. Add Books")
        print("4. Remove Books")
        print("2. List Books")
        print("3. Exit Library")
        choice = input("Choose an option (1-3): ")
    
        if choice == "1":
            book = input("Enter the name of the book: ")
            author = input("Enter the book author: ")
            print(librarian.add_books(book=book,author=author))
        elif choice == "2":
            print(librarian.list_books())
            
        elif choice == "4":
            author = input("Enter the author of the book you want to delete")
            index = input("Enter the index of the book you want to delete")
            print()
        elif choice == "3":
            break
        
        else:
            print("Invalid option. Try again.")
  
    

librarian_action()