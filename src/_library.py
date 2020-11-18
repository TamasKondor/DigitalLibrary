# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

# Create the menu
menu = ConsoleMenu("Digital Library Service", "Please select your role:")

# A SelectionMenu constructs a menu from a list of strings
user_submenu = SelectionMenu(["List contents", "Serch for contents", "Borrow an item", "Return item"])
libr_submenu = SelectionMenu(["Add item", "Modify an item", "Archive a item", "Check borrowed items"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
user_submenu_item = SubmenuItem("User functions", user_submenu, menu)
libr_submenu_item = SubmenuItem("Librarion functions", libr_submenu, menu)

# Once we're done creating them, we just add the items to the menu5

menu.append_item(libr_submenu_item)
menu.append_item(user_submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
menu.join()

sub_user_ret = user_submenu_item.get_return
sub_libr_ret = libr_submenu_item.get_return
selection = menu.selected_option

print("Selected option: ", selection)
print("Selected option: ", sub_user_ret)
print("Selected option: ", sub_libr_ret)

def other():
  sel_index = 3
  while sel_index != "4":
      print("\nWhat would you like to do")
      print("      1  - Add item")
      print("      2  - Modify item")
      print("      3  - List items")
      print("      4  - Exit")
      sel_index = input("Give your selection? ")
      print("\n")

  #if sel_index == "1":
     #addItem(dict_people)
  #elif sel_index == "2":
     #modItem(dict_people)
  #elif sel_index == "3":
   #  for x, y in dict_people.items():
    #    print(x + ": " + y)
  #else:
   #  exit(0)    
