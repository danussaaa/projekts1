# Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!

sk = int(input("Ievadi skaitli:")) 
while sk > 0:
	print(sk)
	sk -= 1
	if sk < 0:
		print("Ievadi naturālu skaitli") #Ja lietotājs ievadfa negatīvu skaitli, progrtamma prasa ievadīt poz skaitli.
	if (sk == 0): #kad lietotājs ievada 0, programma beidz darbu.
		break