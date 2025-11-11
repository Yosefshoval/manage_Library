import moduls.user as us
import moduls.book as bk
import moduls.library as lb
import service.file_handling as fh


def main():
    menu = """ 
            1) Create new user.
            2) Add new book.
            3) Borrow book.
            4) return book
            5) Exit.
            """
# Loading users and books from files
    users = fh.FileHandler.read_file('user', us.User)   # service to library
    books = fh.FileHandler.read_file('book', bk.Book)  # service to library
    
    library = lb.Library()
    library.reset_library(users, books)
    
    # print menu and get user choice
    ask_user = input(menu)

    while ask_user != '5':
        
        match ask_user:
            case '1':
                user = lb.create_user()     # user to library
                library.add_user(user)
                fh.FileHandler.update_file(library.users_list, 'user') # service
            
            case '2':
                book = lb.create_book()
                library.add_book(book)      # book  -> add_to_library
                fh.FileHandler.update_file(library.books_list, 'book') # service 
            
            case '3':                       # to borrow a book: 
                choose = library.choose_user_and_book()   # validation - from library      
                
                if choose[0] and choose[1]:
                    user, book = choose[0], choose[1]
                else:
                    print('Try again')
                    ask_user = input(menu)
                    continue

                library.borrow_book(user, book)            # library
                fh.FileHandler.update_file(library.books_list, 'book') # service -> update in file - the book is unavailable

            case '4':
                choose = library.choose_user_and_book()      # validation - from library      
                
                if choose[0] and choose[1]:
                    user, book = choose[0], choose[1]
                else:
                    print('Try again')
                    ask_user = input(menu)
                    continue
                
                library.return_book(book)               # library
                fh.FileHandler.update_file(library.books_list, 'book') # service -> update in file - the book is available

            case _:
                print('Try again please: ')
                continue

    print('See you next time!!!')


if __name__ == '__main__':
    main()