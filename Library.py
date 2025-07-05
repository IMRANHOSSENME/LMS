class Library:
    __book_list = []

    @classmethod
    def entry_book(self, book):
        if isinstance(book, Book):
            self.__book_list.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library.")
        
    @classmethod
    def get_books(self):
        return self.__book_list

    @classmethod
    def find_id(self, ID):
        for book in self.__book_list:
            if book.get_book_id() == ID:
                return book
        return None



class Book:
    def __init__(self,ID, title, author, status = True):
        self.__ID = ID
        self.__title = title
        self.__author = author
        self.__status = status
        Library.entry_book(self)

    @classmethod
    def view_book_info(self):
        books = Library.get_books()
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print(f"ID: {book.__ID}, Title: {book.__title}, Author: {book.__author}, Availability: {'Available' if book.__status else 'Not Available'}, Author: {book.__author}")


    def get_book_id(self):
        return self.__ID

    def borrow_book(self):
        if not self.__status:
            print(f"Book '{self.__title}' is currently not available.")
        else:
            self.__status = False
            print(f"You have successfully borrowed '{self.__title}'.")


    def return_book(self):
        if self.__status:
            print(f"Book '{self.__title}' is already available.")
        else:
            self.__status = True
            print(f"You have successfully returned '{self.__title}'.")

    




Book(101, "Python Programming", "Imran Hossain", True)
Book(102, "C Programming", "Abdul Karim", True)
Book(103, "Java Programming", "Rakib Hasan", True)
Book(104, "Data Structure", "Bob Brown", True)
Book(105, "Algorithm", "Charlie Davis", True)
Book(106, "Computer Network", "Emily Wilson", True)
Book(107, "Operating System", "Frank Miller", True)
Book(108, "Database Management System", "Grace Lee", True)
Book(109, "Software Engineering", "Hannah White", True)
Book(110, "Web Development", "Ian Green", True)



def main():
    print("Welcome to the Library Management System")
    while True:
        print("\n1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            Book.view_book_info()
        elif choice == '2':
            book_id = int(input("Enter the book ID to borrow: "))
            book = Library.find_id(book_id)
            if book:
                book.borrow_book()
            else:
                print("Book not found.")
        elif choice == '3':
            book_id = int(input("Enter the book ID to return: "))
            book = Library.find_id(book_id)
            if book:
                book.return_book()
            else:
                print("Book not found.")
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()