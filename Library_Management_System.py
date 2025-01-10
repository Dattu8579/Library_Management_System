import os

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        """Load books from a file."""
        if os.path.exists("books.txt"):
            with open("books.txt", "r") as file:
                for line in file:
                    title, author, year, isbn = line.strip().split(",")
                    self.books.append(Book(title, author, year, isbn))

    def save_books(self):
        """Save books to a file."""
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year},{book.isbn}\n")

    def add_book(self):
        """Add a new book to the library."""
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book publication year: ")
        isbn = input("Enter book ISBN: ")

        book = Book(title, author, year, isbn)
        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        """View all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")

    def search_book(self):
        """Search for a book by title or author."""
        search_term = input("Enter title or author to search: ").lower()
        found_books = [book for book in self.books if search_term in book.title.lower() or search_term in book.author.lower()]
        
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No matching books found.")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search for a Book")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
