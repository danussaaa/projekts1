import sqlite3
connection = sqlite3.connect('skola.db')
#izveidot programmu, kas ļauj ievadīt informāciju par atzīmēm

# un saglabā to tabulā

import sqlite3

connection = sqlite3.connect("skola.db")

cursor = connection.cursor()

while True:

    ko_darit = int(input('''Ko darīt?

                    1 - ievadīt informāciju

                    2 - beigt darbu\n'''))

   

    if ko_darit == 1:

        prieksm = input('ievadi prieksmeta nosaukumu: ')

        atzime = int(input('Ievadi atzīmi: '))

        skid = int(input('Ievadi skolēna id: '))

        cursor.execute("INSERT INTO atzimes (prieksmets, atzime, skolenaID) VALUES(?,?,?) ", (prieksm, atzime, skid))

   

   

    elif ko_darit == 2:

        connection.commit()

        connection.close()

        exit()