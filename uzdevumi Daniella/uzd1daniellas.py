# Lietotājs ievada vairākus skaitļus. Ievade beidzas, kad lietotājs ir ievadījis skaitli 0. 
#Izvadi visu iepriekš ievadīto skaitļu aritmētisko vidējo!
sk = int(input("Ievadi skaitli (0-beigt):")) 
summa = 0
skaits = 0

while sk != 0: 
	summa += sk 
	skaits += 1
	sk = float(input("Ievadi skaitli (0-beigt):"))
	#int nomaina ar float, lai var ievadīt arī decimāldaļas

print("Visu ievadito skaitlu aritmetiskais videjais ir", summa / skaits)