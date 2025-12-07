class Book:
    """
    A class to represent a book, demonstrating Python magic methods.
    """

    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' has been created.")

    def __str__(self):
        """
        String Representation: Returns a user-friendly, informal string.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns an unambiguous string that
        could be used to recreate the object.
        Format: "Book('title', 'author', year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

# Note: The provided main.py will handle object creation, method calls, and deletion.