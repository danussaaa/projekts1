skaits=  1
while skaits < 1 or skaits > 8 :
    skaits = int(input('ievadiet skaitli '))

k = 1
for i in range(1,skaits + 1):
    print(" " * skaits - i, end='')
    print('#' * i)
 