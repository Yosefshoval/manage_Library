import uuid
import user as us
import book as bk


class Library:
    def __init__(self, ):
        self.users_list = []
        self.books_list = []
    
    
    def add_book(self, book):
        self.books_list.append(book)
    

    def add_user(self, user):
        self.users_list.append(user)
    

    def find_user_and_book(self, user_id, book_isbn):
        user = None
        for current_user in self.users_list:
            if current_user.id == user_id:
                user = current_user
                break
        
        book = None
        for currebt_book in self.books_list:
            if currebt_book.isbn == book_isbn:
                book = currebt_book
                break
        return book, user


    def borrow_book(self, user, book):
        book.is_available = False
        user.add_borrowed_book(book)
        return True
    
    
    def return_book(self, book):
        book.is_available = True
        return True


    def search_book(self, title=None, auther=None):
        pass


    def reset_library(self, users, books):
        self.users_list = users
        self.books_list = books

    def choose_user_and_book(self):
        user = input('Prase your name: ')
        book = input('Prase book title or auther: ')
        
        return self.find_user_and_book(user, book) # get objects of user and book


def create_user():
    """ respons name of user and create User object """
    name = input('Enter your name: ')
    id = uuid.uuid4()
    user = us.User(name, id)
    return user


def create_book():
    title = input('Enter the book title: ')
    auther = input('Enter the book auther: ')
    isbn = uuid.uuid4()
    book = bk.Book(title, auther, isbn)
    return book
