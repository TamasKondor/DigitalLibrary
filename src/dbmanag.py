import sqlite3

def getConnection(db_file=r"D:\PythonTraining\ProjectWork\db\DigitalLibraryDB.db"):
    """ Create a database connection to the SQLite database specified by db_file
    param  -  db_file: database file
    return -  Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)        
        return conn
    except sqlite3.Error as e:
        print("Failed to connect to sqlite database!", e)    
    return conn


def getTableContent(conn, table_name):
    """ Select user table content  
        Return list of dictionary       
    """
    resarr = []       
    colNames = []
    try:
        cursor = conn.cursor()
        select_query = "SELECT * from {}".format(table_name)
        cursor.execute(select_query)

        # Get column names into a list
        for colName in cursor.description:
            colNames.append(colName[0])
        ColNr = len(colNames)
        
        records = cursor.fetchall()
        # print("Total rows in ", table_name, " table:  ", len(records))
        for row in records:
            resd = {}
            for x in range(ColNr):
                resd[colNames[x]] = row[x]
            resarr.append(resd)
        cursor.close()
        return resarr

    except sqlite3.Error as e:
        print("Failed to read data from sqlite table!", e)    
    finally:
         pass

def closeConnection(conn):
    if (conn):
        conn.close()
        print("The databese connection is closed")
    else:
        print("No connection was defined.")


def local_main():
    database = r"D:\PythonTraining\ProjectWork\db\DigitalLibraryDB.db"

    # create a database connection
    conn = getConnection(database)

    # Read User table if connection is OK
    if conn is not None:
        # read User table
        uList = getTableContent(conn, "user")
        for u in uList:
            print(u) 

        # read Type table
        tList = getTableContent(conn, "type")
        for t in tList:
           print(t)    

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    local_main()