Rem # This script creates the initial Digital Library database
Rem ###########################################################

sqlite3.exe ..\db\DigitalLibraryDB.db ".read  _createDatabase.sql"