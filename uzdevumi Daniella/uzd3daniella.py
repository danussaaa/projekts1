# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!

saraksts = input("Ievadi skaitlus, atdalot tos ar atstarpi:")
sk = list(map(int, saraksts.split())) #izveido ievadīto skaitļu sarakstu.

dub = set () #mainīgais vienādiem skaitļiem.

for sks in sk:
	if sk.count(sks) > 1:
		dub.add(sks)

if dub:
	print("Vienādie skaitļi:", ','.join(map(str,dub))) #izvada vienādo skaitļu sarakstu, ja tāds ir.
else:
	print("Nav vienādu skaitļu!")

