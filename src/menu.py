import dbmanag
from consolemenu import SelectionMenu


def show_UserMenu():
    user_list = ["List all contents", "Serch for contents", "Borrow an item", "Return item"]
    selection_usr = SelectionMenu.get_selection(user_list, "Digital Library Service - User Functions", "Please select function:")
    return selection_usr

def show_LibrMenu():
    libr_list = ["Add item", "Update item", "Archive a item", "Check borrowed items"]
    selection_lib = SelectionMenu.get_selection(libr_list, "Digital Library Service - Librarian Functions", "Please select function:")
    return selection_lib

    
def show_MainMenu():    
    main_list = ["User functions", "Librarioan functions"]
    selection_main = SelectionMenu.get_selection(main_list, "Digital Library Service", "Please select your role:")
    return selection_main

def show_Contents(lstContents):     
    lst_ContForm = []        
    for cnt in lstContents.contentList:
       lst_ContForm.append(cnt.getListItem())

    subTitle = '{0:<41} {1:<23} {2:<2}'.format( "      Name", "Author", "In")
    menu = SelectionMenu(lst_ContForm, "Digital Library Contents", subTitle, show_exit_option=False)    
    menu.show()
    menu.join()    
    return menu.selected_option


def funcUserMenu(option, lstContents):
    print("User function: {}".format(option))    

    if option == 0:        
        print("Listing content")
        show_Contents(lstContents)        
    elif option == 1:
        print("Searching content")
    elif option == 2:
        print("Borrowing item")
    elif option == 3:
        print("Returning item")
    else:
        print("Exiting menu...")


def funcLibrarianMenu(option):
    print("Librarian function: {}".format(option))
    if option == 0:
        print("Adding item")
    elif option == 1:
        print("Update item data")
    elif option == 2:
        print("Archiving item")
    elif option == 3:
        print("Checking borrowed item")
    else:
        print("Exiting menu...")


def menu_main():
   show_MainMenu()
   # show_UserMenu()
   # show_LibrMenu()

if __name__ == '__main__':    
    menu_main()
   

