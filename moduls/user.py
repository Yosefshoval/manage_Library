class User:
    def __init__(self, name, id, borrowed_books=[]):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books

    def add_borrowed_book(self, book):
        self.borrowed_books.append(book)