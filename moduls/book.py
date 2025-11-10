class Book:
    def __init__(self, title, author, ISBN, is_available = True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = is_available
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Available: {self.is_available}"
