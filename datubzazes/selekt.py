import sqlite3
connection = sqlite3.connect('skola.db')
#izveidot programmu, kas ļauj ievadīt informāciju par atzīmēm

# un saglabā to tabulā

import sqlite3

connection = sqlite3.connect("skola.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM sklolens Where vards LIKE 'D%'")

dati = cursor.fetchall()

for rinda in dati:
    print(rinda)


connection.commit