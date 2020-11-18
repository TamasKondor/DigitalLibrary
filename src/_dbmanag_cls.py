import sqlite3

class DatabaseMng ():  
    db_name = "none"
    db_conn = None
    cursor = None
    query_txt = ""
    records = []

    def __init__(self, name):
        self.db_name = name

    def create_connection(self):
        """ Create a database connection to the SQLite database specified by db_file
        param  -  db_file: database file
        return -  Connection object or None
        """
        # self.conn = None
        self.db_name = sqlite3.connect(self.db_name)            
        #try:
        #    self.conn = sqlite3.connect(self.db_name)            
        #    return self.conn
        #except sqlite3.Error as e:
        #    print("Failed to connect to sqlite database!", e)    
        #return self.conn


    def read_user_table(self, table_name):
        """ Select table content  
        """
        try:
            self.cursor = db_name.cursor()
            self.select_query = """SELECT * from user"""
            self.cursor.execute(self.select_query)
            self.records = self.cursor.fetchall()
            print("Total rows are:  ", len(self.records))
            print("Printing each row")
            for self.row in self.records:
                print("Id: ", self.row[0])
                print("Name: ", self.row[1], " ", self.row[2])
                print("Added: ", self.row[3])
                print("Role: ", self.row[4])

            self.cursor.close()

        except sqlite3.Error as e:
            print("Failed to read data from sqlite table!", e)    
        finally:
             if (self.db_conn):
                self.db_conn.close()
                print("The databese connection is closed")




digLibDB = DatabaseMng(r"D:\PythonTraining\ProjectWork\db\DigitalLibraryDB.db")
 
# create a database connection
digLibDB.create_connection

print(digLibDB.__dict__)

# Read table content if connection is OK
# if db_conn is not None:   
digLibDB.read_user_table("user")
# else:
#    print("Error! cannot create the database connection.")


