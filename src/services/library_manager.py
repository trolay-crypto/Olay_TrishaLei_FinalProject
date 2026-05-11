from models.book import Book
from services.file_handler import FileHandler


class LibraryManager:
    """
    Handles all library functions.
    """

    def __init__(self):
        self.books = []

        data = FileHandler.load_data()

        for item in data:
            book = Book(
                item["title"],
                item["author"],
                item["status"]
            )

            self.books.append(book)

    def add_book(self, title, author):
        """
        Adds a new book.
        """
        book = Book(title, author)

        self.books.append(book)

        self.save_books()

    def view_books(self):
        """
        Displays all books.
        """
        if not self.books:
            print("\nNo books available.\n")
            return

        print("\nBOOK LIST")
        print("-" * 40)

        for book in self.books:
            print(book)

        print()

    def search_book(self, title):
        """
        Searches books by title.
        """
        results = [
            book for book in self.books
            if title.lower() in book.title.lower()
        ]

        if not results:
            print("\nBook not found.\n")
            return

        print("\nSEARCH RESULTS")
        print("-" * 40)

        for book in results:
            print(book)

        print()

    def borrow_book(self, title):
        """
        Borrows a book.
        """
        for book in self.books:
            if book.title.lower() == title.lower():

                if book.status == "Borrowed":
                    print("Book is already borrowed.\n")
                    return

                book.status = "Borrowed"

                self.save_books()

                print("Book borrowed successfully!\n")
                return

        print("Book not found.\n")

    def return_book(self, title):
        """
        Returns a borrowed book.
        """
        for book in self.books:
            if book.title.lower() == title.lower():

                if book.status == "Available":
                    print("Book is already available.\n")
                    return

                book.status = "Available"

                self.save_books()

                print("Book returned successfully!\n")
                return

        print("Book not found.\n")

    def show_total_books(self):
        """
        Displays the total number of books.
        """
        total = len(self.books)

        print(f"\nTotal Books: {total}\n")

    def save_books(self):
        """
        Saves books to JSON file.
        """
        data = [book.to_dict() for book in self.books]

        FileHandler.save_data(data)