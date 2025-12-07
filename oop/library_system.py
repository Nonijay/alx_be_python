## Inheritance: Base Class
class Book:
    """Base class for all books."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

## Inheritance: Derived Classes
class EBook(Book):
    """Represents a digital book with a file size."""
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """Represents a physical book with a page count."""
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

## Composition: Container Class
class Library:
    """Manages a collection of Book objects, demonstrating composition."""
    def __init__(self):
        # The 'books' list is composed of Book, EBook, and PrintBook instances
        self.books = []

    def add_book(self, book):
        """Adds a Book or derived class instance to the library."""
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """Prints the details of each book in the library."""
        print("\n--- Library Collection ---")
        for book in self.books:
            # Check the type to print specific attributes (Polymorphism)
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")
        print("--------------------------")