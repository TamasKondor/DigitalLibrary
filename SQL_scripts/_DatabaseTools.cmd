Rem # This script dump the entire database and load it back to DB
Rem #############################################################

Rem # Dump the entire database to an SQL file
sqlite3.exe ..\db\DigitalLibraryDB.db .dump > ..\db\dumped_DB.sql

Rem #Import the dumped content back to database
REM sqlite3.exe ..\db\DigitalLibraryDB.db < ..\db\dumped_DB.sql
