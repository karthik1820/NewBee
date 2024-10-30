# Step 1: Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' has been returned.")

# Step 2: Define the Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def remove_book(self, book):
        self.books.remove(book)
        print(f"Removed '{book.title}' from the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"'{title}' not found in the library.")
        return None

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} by {book.author} - {status}")

# Step 3 (Optional): Define the Member class
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def borrow_book(self, book):
        book.borrow_book()

    def return_book(self, book):
        book.return_book()





# Create books
book1 = Book("Python Programming", "John Doe", "12345")
book2 = Book("Data Science 101", "Jane Smith", "67890")

# Create a library and add books
library = Library()
library.add_book(book1)
library.add_book(book2)

# # Display books
# library.display_books()

# # Borrow and return books
# book1.borrow_book()
# library.display_books()

# book1.return_book()
library.display_books()
