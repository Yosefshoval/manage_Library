import moduls.user as us
import moduls.book as bk
import moduls.library as lb
import service.file_handling as fh
import service.initializing_systam as ins


def main():
    menu = """ 
            1) Create new user.
            2) Add new book.
            3) Borrow book.
            4) return book.
            5) search book.
            6) Exit.
            """
    # Loading users and books from files
    library = ins.create_library()
    
    # print menu and get user choice
    ask_user = None

    while ask_user != '6':
        ask_user = input(menu)

        match ask_user:
            case '1':
                user = lb.create_user()
                print(user.name, 'created')
                library.add_user(user)
                fh.FileHandler.update_file(library.users_list, 'user')
            
            case '2':
                book = lb.create_book()
                library.add_book(book)
                fh.FileHandler.update_file(library.books_list, 'book')
            
            case '3':
                choose = library.choose_user_and_book()      
                
                if choose[0] and choose[1]:
                    user, book = choose[0], choose[1]
                else:
                    print('User or Book not found.')
                    continue

                library.borrow_book(user, book)
                fh.FileHandler.update_file(library.books_list, 'book')

            case '4':
                choose = library.choose_user_and_book()
                
                if choose[0] and choose[1]:
                    user, book = choose[0], choose[1]
                else:
                    print('Try again')
                    ask_user = input(menu)
                    continue
                
                library.return_book(book)               # library
                fh.FileHandler.update_file(library.books_list, 'book') # service -> update in file - the book is available

            case '5':
                title = input('Enter title or auther: ')
                book_list = library.search_book(title=title)
                print(book_list)
            
            case _:
                print('Try again please: ')
                continue

    print('See you next time!!!')
