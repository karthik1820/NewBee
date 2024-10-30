class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"book is taken '{self.title}'")
        else:
            print(f"book is available '{self.title}'")
        
    def return_book(self):
        self.is_available = True
        print ("book returned")

class Librarry:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def remove_book(self,book):
        self.books.remove(book)
        print(f"book removed from the lib --> '{book.title}'")

    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                return book
            print(f"book not found --> {book}")
            return None
    
    def display_books(self):
        print("books in lib")
        for book in self.books:
            status = "Available" if book.is_available else "Not available"
            print(f"{book.title} by {book.author} - {status}")



        # for book in self.books:
        #     status = "Available" if book.is_available else "Not Available"
        #     print(f"{book.title} by {book.author} - {status}")




book1 = Book("Python Programming", "John Doe", "12345")
book2 = Book("Data Science 101", "Jane Smith", "67890")
book3 = Book("FF1","paul", "11111")



Librarry = Librarry()

Librarry.add_books(book2)
Librarry.add_books(book1)
Librarry.add_books(book3)
Librarry.add_books(book3)
print("-------------------")
book3.borrow_book()
Librarry.display_books()


print("-------------------")
book3.return_book()
Librarry.display_books()

