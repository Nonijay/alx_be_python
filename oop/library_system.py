## Inheritance: Base Class
class Book:
    """Base class for all books."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns the user-friendly string representation of the Book."""
        return f"Book: {self.title} by {self.author}"

## Inheritance: Derived Classes
class EBook(Book):
    """Represents a digital book with a file size."""
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns the user-friendly string representation of the EBook."""
        # Use super().__str__() to get the base details and append the EBook specific detail
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Represents a physical book with a page count."""
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns the user-friendly string representation of the PrintBook."""
        # Use super().__str__() to get the base details and append the PrintBook specific detail
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

## Composition: Container Class
class Library:
    """Manages a collection of Book objects, demonstrating composition."""
    def __init__(self):
        # The 'books' list is composed of Book, EBook, and PrintBook instances
        self.books = []

    def add_book(self, book):
        """Adds a Book or derived class instance to the library."""
        self.books.append(book)
        # Note: Removing the 'print' statement here to strictly match the final expected output format
        # print(f"Added '{book.title}' to the library.") 

    def list_books(self):
        """Prints the details of each book in the library using polymorphism (via __str__)."""
        for book in self.books:
            # Polymorphism: print(book) automatically calls book.__str__()
            print(book)