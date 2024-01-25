#Javeido programma, kas atkarībā no ievadita diennakts laika sasveicinas ar lietotaju
#ievade notiek formata 12:45
#rīts: no 5:00 līdz 10:59 ieskaitot
#diena: no 11:00 līdz 18:59 ieskaitot
#vakars: no 19:00 līdz 22:59 ieskaitot
#nakts: no 23:00 līdz 4:59 ieskaitot

time = input("Ievadi laiku: ")

if "4:00" < time < "10:00":
    print("Labrīt!")
elif "16:00" > time > "10:00":
    print("Labdien!")
elif "22:00" > time > "16:00":
    print("Labvakar!")
elif "22:00" < time < "4:00":
    print("Labu nakti!")
else:
    print("Šāda laika nav!")