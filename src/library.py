from os import system
from getpass import getpass
from objects import *
import dbmanag
import menu

# Doing proper clousre before leaving the application
def app_exit(conn):
    dbmanag.closeConnection(conn)
    exit()

# Entry point of the application

# Definition of lists containing record from DB
lst_contentObj = []
lst_typeObj = []
lst_userObj = []

# Get DB connection object
db_conn = dbmanag.getConnection()

# Load user records to Users collection (list of User objects)
lst_user = dbmanag.getTableContent(db_conn, "user")
libUsers = Users(lst_user)

# Load content records to Contents collection (list of Content objects)
lst_content = dbmanag.getTableContent(db_conn, "content")
libContents = Contents(lst_content)

# Load type records to ContType collection (list of ContType objects)
lst_type = dbmanag.getTableContent(db_conn, "type")
libTypes = ContTypes(lst_type)

#   print(obj_cont.contentid, obj_cont.name, "(", lst_type[obj_cont.typeid]["TypeName"], ")")
# userObj = libUsers.getUserByAccount("tiacs")
# print(userObj.fullname)

# Start the screen operations
clear = lambda: system('clear')   # Clear the screen

# Draw the title
print("=" * 44)
print("   WELCOME TO THE DIGITAL LIBRARY SERVICE")
print("=" * 44)
print("\n")

vTryNr = 0
vLoggedIn = False
while vLoggedIn != True:

   # Check the number of attempts   
   vTryNr += 1
   if vTryNr > 3:
      print("Maximum 3 attempts allowed to provide account!")
      print("Leaving library services...")      
      app_exit(db_conn)   
   
   # Ask for user account
   # vUserAcc = "tiacs"
   vUserAcc = input("Please enter your user account:")
   
   # Check whether the User object exists
   curUser = libUsers.getUserByAccount(vUserAcc)

   if curUser is not None:
      print(curUser.fullname)
      vLoggedIn = True      
   else:      
      print("User account does not exist. Please try again.")
      vLoggedIn = False      

vTryNr = 0
vLoggedIn = False
while vLoggedIn != True:
   
   # Check the number of attempts
   vTryNr += 1
   if vTryNr > 3:
      print("Maximum 3 attempts allowed to provide pasword!")
      print("Leaving library services...")      
      app_exit(db_conn)

   # Ask for password
   # vUserPwd = "t"
   vUserPwd = getpass()
   

   if curUser.pwd == vUserPwd:
      print("Welcome back " + curUser.fullname)
      vLoggedIn = True      
   else:
      print("Invalid password! Please try again.")
      vLoggedIn = False      


# show Main Menu
# menu.show_MainMenu(curUser.role)
if curUser.role == "Librarian":
   retm = menu.show_MainMenu()
   if retm == 0:
      retm = menu.show_UserMenu()
      menu.funcUserMenu(retm, libContents)
   elif retm == 1:
      retm = menu.show_LibrMenu()
      menu.funcLibrarianMenu(retm)
   else:
      pass      
else:
   retm = menu.show_UserMenu()
   menu.funcUserMenu(retm, libContents)

tmp = input("Press Enter to continue...")

   





