import json
import os

ALL_BOOKS = "books.json"

def load_books():
    if os.path.exists(ALL_BOOKS):
        with open(ALL_BOOKS, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(ALL_BOOKS, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Book added successfully!\n")

def view_books():
    books = load_books()
    if not books:
        print("No books found.\n")
    else:
        print("Book List:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']}")
        print("")

def delete_book():
    view_books()
    books = load_books()
    try:
        choice = int(input("Enter the number of the book to delete: ")) - 1
        if 0 <= choice < len(books):
            removed_book = books.pop(choice)
            save_books(books)
            print(f"Deleted '{removed_book['title']}' successfully!\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("Book Manager CLI")
        print("1. Add a book")
        print("2. View books")
        print("3. Delete a book")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()

