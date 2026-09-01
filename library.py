from itertools import count


class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print("Book issued successfully")
        else:
            print("Book already issued")

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            print("Book returned successfully")
        else:
            print("Book is not issued")

    def show_book(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

        if self.is_issued:
            print("Status: Issued")
        else:
            print("Status: Available")


class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def show_member(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")

        if self.borrowed_books:
            print("Borrowed Books:")

            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print("No borrowed books")


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    # ---------------- BOOK METHODS ----------------

    def add_book(self, book):

        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Book ID already exists")
                return

        self.books.append(book)
        print("Book added successfully")

    def show_books(self):

        if not self.books:
            print("No books found")
            return

        for book in self.books:
            book.show_book()
            print("--------------------")

    def search_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                book.show_book()
                return

        print("Book not found")

    def delete_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                if book.is_issued:
                    print("Cannot delete an issued book")
                    return

                self.books.remove(book)
                print("Book deleted successfully")
                return

        print("Book not found")

    def total_books(self):
        print(f"Total Books: {len(self.books)}")

    def total_available_books(self):
     count = 0

     for book in self.books:
        if not book.is_issued:
            count += 1

    print(f"Available Books: {count}")    

    # ---------------- MEMBER METHODS ----------------

    def add_member(self, member):

        for existing_member in self.members:

            if existing_member.member_id == member.member_id:
                print("Member ID already exists")
                return

        self.members.append(member)
        print("Member added successfully")

    def show_members(self):

        if not self.members:
            print("No members found")
            return

        for member in self.members:
            member.show_member()
            print("--------------------")

    def search_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:
                member.show_member()
                return

        print("Member not found")

    def delete_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:

                if member.borrowed_books:
                    print("Cannot delete member with borrowed books")
                    return

                self.members.remove(member)
                print("Member deleted successfully")
                return

        print("Member not found")

    def total_members(self):
        print(f"Total Members: {len(self.members)}")

    # ---------------- ISSUE BOOK ----------------

    def issue_book(self, book_id, member_id):

        selected_book = None
        selected_member = None

        for book in self.books:

            if book.book_id == book_id:
                selected_book = book
                break

        if selected_book is None:
            print("Book not found")
            return

        for member in self.members:

            if member.member_id == member_id:
                selected_member = member
                break

        if selected_member is None:
            print("Member not found")
            return

        if selected_book.is_issued:
            print("Book already issued")
            return

        selected_book.issue_book()
        selected_member.borrowed_books.append(selected_book)

    # ---------------- RETURN BOOK ----------------

    def return_book(self, book_id, member_id):

        selected_book = None
        selected_member = None

        for book in self.books:

            if book.book_id == book_id:
                selected_book = book
                break

        if selected_book is None:
            print("Book not found")
            return

        for member in self.members:

            if member.member_id == member_id:
                selected_member = member
                break

        if selected_member is None:
            print("Member not found")
            return

        if selected_book not in selected_member.borrowed_books:
            print("This member does not have this book")
            return

        selected_book.return_book()
        selected_member.borrowed_books.remove(selected_book)

    # ---------------- ISSUED BOOKS ----------------

    def show_issued_books(self):

        found = False

        for book in self.books:

            if book.is_issued:
                book.show_book()
                print("--------------------")
                found = True

        if not found:
            print("No books are currently issued")


# ==================================================
#                LIBRARY OBJECT
# ==================================================

library1 = Library()


# ==================================================
#                    MAIN MENU
# ==================================================

while True:

    print("\n======================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Member")
    print("6. Show Members")
    print("7. Search Member")
    print("8. Delete Member")
    print("9. Issue Book")
    print("10. Return Book")
    print("11. Total Books")
    print("12. Total Members")
    print("13. Show Issued Books")
    print("14. Exit")

    choice = input("Enter your choice: ")

    # ADD BOOK
    if choice == "1":

        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library1.add_book(book)

        except ValueError:
            print("Book ID must be a number")

    # SHOW BOOKS
    elif choice == "2":

        library1.show_books()

    # SEARCH BOOK
    elif choice == "3":

        try:
            book_id = int(input("Enter Book ID: "))
            library1.search_book(book_id)

        except ValueError:
            print("Book ID must be a number")

    # DELETE BOOK
    elif choice == "4":

        try:
            book_id = int(input("Enter Book ID: "))
            library1.delete_book(book_id)

        except ValueError:
            print("Book ID must be a number")

    # ADD MEMBER
    elif choice == "5":

        try:
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Member Name: ")

            member = Member(member_id, name)
            library1.add_member(member)

        except ValueError:
            print("Member ID must be a number")

    # SHOW MEMBERS
    elif choice == "6":

        library1.show_members()

    # SEARCH MEMBER
    elif choice == "7":

        try:
            member_id = int(input("Enter Member ID: "))
            library1.search_member(member_id)

        except ValueError:
            print("Member ID must be a number")

    # DELETE MEMBER
    elif choice == "8":

        try:
            member_id = int(input("Enter Member ID: "))
            library1.delete_member(member_id)

        except ValueError:
            print("Member ID must be a number")

    # ISSUE BOOK
    elif choice == "9":

        try:
            book_id = int(input("Enter Book ID: "))
            member_id = int(input("Enter Member ID: "))

            library1.issue_book(book_id, member_id)

        except ValueError:
            print("ID must be a number")

    # RETURN BOOK
    elif choice == "10":

        try:
            book_id = int(input("Enter Book ID: "))
            member_id = int(input("Enter Member ID: "))

            library1.return_book(book_id, member_id)

        except ValueError:
            print("ID must be a number")

    # TOTAL BOOKS
    elif choice == "11":

        library1.total_books()

    # TOTAL MEMBERS
    elif choice == "12":

        library1.total_members()

    # ISSUED BOOKS
    elif choice == "13":

        library1.show_issued_books()

    # EXIT
    elif choice == "14":

        print("Thank you for using Library Management System!")
        break

    # INVALID CHOICE
    else:

        print("Invalid choice. Please try again.")

        print("Invalid choice. Please try again.")

        