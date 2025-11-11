from moduls.book import Book
from moduls.user import User
from moduls.library import Library
import service.file_handling as fh



def create_library():
    users = fh.FileHandler.read_file('user', User)
    books = fh.FileHandler.read_file('book', Book)

    library = Library()
    library.reset_library(users, books)

    return library