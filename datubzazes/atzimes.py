
import sqlite3
 
# Connecting to sqlite
# connection object
connection = sqlite3.connect('skola.db')
 
# cursor object
cursor = connection.cursor()
 
# Drop the GEEK table if already exists.
cursor.execute("CREATE TABLE atzimes (ID INTEGER PRIMARY KEY AUTOINCREMENT)")
 
# izveido tabulu
table =  ("CREATE TABLE atzimes ( ID INTIGER NOT NULL,PRIMARY KEY, AUTOINCREMENT, prieksmets TEXT, skolenaID INTEGER, FOREIGN KEY (skolenaID) REFERENCES sklolens(ID)")

 
print("Table is Ready")
 
# Close the connection
connection.close()