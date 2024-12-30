class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1
        print(f"Added '{book_name}' to the library.")

    def view_books(self):
        if not self.books:
            print("No books are available in the library.")
        else:
            print("Available books:")
            for book, count in self.books.items():
                print(f"{book} - {count} copy(ies)")

    def borrow_book(self, book_name):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(f"You have borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is not available or out of stock.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1
        print(f"Returned '{book_name}' to the library.")

def main():
    library = Library("Community Library")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the book name to add: ")
            library.add_book(book_name)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            book_name = input("Enter the book name to borrow: ")
            library.borrow_book(book_name)
        elif choice == '4':
            book_name = input("Enter the book name to return: ")
            library.return_book(book_name)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()