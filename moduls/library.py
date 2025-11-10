
class Library:
    def __init__(self, ):
        self.users_list = []
        self.books_list = []
    
    
    def add_book(self, book):
        self.books_list.append(book)
    

    def add_user(self, user):
        self.users_list.append(user)
    

    def find_user_and_book(self, user_id, book_isbn):
        valid_user = map(lambda u: u.id == user_id, self.users_list)
        user = next(valid_user, None)
        valid_book = map(lambda b: b.isbn == book_isbn, self.books_list)
        book = next(valid_book, None)
        return book, user

        
        # for current_user in self.users_list:
        #     if current_user.id == user_id:
        #         user = current_user
                # break
        
        # book = None
        # for currebt_book in self.books_list:
        #     if currebt_book.isbn == book_isbn:
        #         book = currebt_book
        #         break
        


    def borrow_book(self, user_id, book_isbn):
        book, user = self.find_user_and_book(user_id, book_isbn)
        book.is_available = False
        user.add_borrowed_book(book)
        return True
    
    
    def return_book(self, user_id, book_isbn):
        book, user = self.find_user_and_book(user_id, book_isbn)
        book.is_available = True
        
        return True


    def search_book(self, title, auther):
        results = []
        for book in self.books_list:
            results.extend(book for book in self.books_list if book.title.lower() == title.lower() or book.auther.lower() == auther.lower())
        if not results:
            return None   
        return results
        


    def reset_library(self, users, books):
        self.users_list = users
        self.books_list = books