def main():
    menu = """ 
            1) 
            2) 
            3) 
            4)
            5)
            """
    ask_user = input(menu)
    library = Library()

    read_books() # service to library
    read_users() # service to library
    
    reset_library(read_books, read_users)
    
    while ask_user != '5':
        
        match ask_user:
            case '1':
                create_user()            # user to library      add_to_library()  # library
                update_file(file='user') # service
            
            case '2':
                add_book()               # book  -> add_to_library
                update_file(file='book') # service 
            
            case '3':                    # to borrow a book: 
                choose_user_and_book()   # validation - from library      
                borrow()                 # library
                update_file(file='book') # service -> update in file - the book is unavailable

            case '4':
                choose_user_and_book()   # validation - from library      
                return_book()            # library
                update_file(file='book') # service -> update in file - the book is available

            case _:
                ask_user = input('Try again please: ')
                continue
        ask_user = input(menu)



if __name__ == '__main__':
    pass


