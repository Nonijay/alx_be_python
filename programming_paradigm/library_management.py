# library_management.py

class Book:
    """Represents a book with public title/author and private availability status."""
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute for encapsulation
        self._is_checked_out = False 

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for easy printing."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        # Private list for encapsulation: stores Book instances
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        print(f"Added: {book.title}")

    def _find_book(self, title):
        """Internal helper to find a Book object by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """Finds a book and marks it as checked out if available."""
        book_to_check_out = self._find_book(title)
        
        if book_to_check_out:
            if book_to_check_out.check_out():
                print(f"Checked out: {title}")
                return True
            else:
                print(f"Error: '{title}' is already checked out.")
        else:
            print(f"Error: Book titled '{title}' not found in library.")
        return False

    def return_book(self, title):
        """Finds a book and marks it as available."""
        book_to_return = self._find_book(title)
        
        if book_to_return:
            if book_to_return.return_book():
                print(f"Returned: {title}")
                return True
            else:
                print(f"Error: '{title}' was already available.")
        else:
            print(f"Error: Book titled '{title}' not found in library.")
        return False

    def list_available_books(self):
        """Prints the title and author of all available (not checked out) books."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_count += 1
        if available_count == 0:
            print("No books are currently available.")