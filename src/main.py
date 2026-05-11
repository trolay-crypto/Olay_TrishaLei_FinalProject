from services.library_manager import LibraryManager


def display_menu():
    """
    Displays the main menu.
    """
    print("==== PERSONAL LIBRARY ORGANIZER ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show Total Books")
    print("7. Exit")


def main():
    """
    Main program loop.
    """
    library_system = LibraryManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            library_system.add_book(title, author)

            print("Book added successfully!\n")

        elif choice == "2":
            library_system.view_books()

        elif choice == "3":
            title = input("Enter title to search: ")

            library_system.search_book(title)

        elif choice == "4":
            title = input("Enter title to borrow: ")

            library_system.borrow_book(title)

        elif choice == "5":
            title = input("Enter title to return: ")

            library_system.return_book(title)

        elif choice == "6":
            library_system.show_total_books()

        elif choice == "7":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()