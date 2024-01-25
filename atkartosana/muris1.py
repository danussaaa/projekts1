skaits = 0          #izveido mainīgo

#skaits = int(input('ievadiet skaitli '))   #piedāvā ievadīt skaitli

while skaits < 1 or skaits > 8 :   #atlauj iuevadit tikai skaitli no 1 lidz 8
    skaits = int(input('ievadiet skaitli '))


for i in range(skaits):
    print('#', end = ' ')