import sqlite3

connection = sqlite3.connect("skola.db") #pievieno SQLITE3 noteikto datu bāzi
cursor = connection.cursor()

cursor.execute("INSERT INTO sklolens(vards,uzvards,klasesID) VALUES('Elza','Dumbre','1')")
connection.commit() #izmainas saglaba dqatubāzē
connection.close