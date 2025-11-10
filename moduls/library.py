
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


    def borrow_book(self, user_id, book_isbn):
        book, user = self.find_user_and_book(user_id, book_isbn)
        book.is_available = False
        user.add_borrowed_book(book)
        return True
    
    
    def return_book(self, user_id, book_isbn):
        book, user = self.find_user_and_book(user_id, book_isbn)
        book.is_available = True
        
        return True


    def search_book(self, title=None, auther=None):
        pass