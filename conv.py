#coding:utf-8
reponce = "oui"
while reponce == "oui":
	monnaie=input("De quelle monnaie disposez vous ? Dollars, FCFA, Euro, yuan ")
	monnaie=str(monnaie)

	devise=input("En quelle devise voulez vous là changer ?   ")
	devise=str(devise)
	print(" ")
	print("***********PRESENTATION DES TAUX DE CHANGE*************")
	print(" ")
	print("1 Dollars = 550FCFA")
	print("1 Euro = 600 FCFA")
	print("1 Dollars = 2 Euro")
	print("1 yuan = 88 FCFA")
	print("1 yuan = 0.14 Dollars ")
	print(" ")

	montant=input("Entrez le montant que vous voulez changer:    ")
	montant=int(montant)
	

	if monnaie=="Dollars" and devise=="FCFA":
		resultat==montant*550
		resultat=float(resultat)

	elif monnaie=="FCFA" and devise=="Dollars":
		resultat=montant/550
		resultat=float(resultat)

	elif monnaie=="Euro" and devise=="FCFA":
		resultat=montant*600
		resultat=float(resultat)

	elif monnaie=="FCFA" and devise=="Euro":
		resultat=montant/600
		resultat=float(resultat)

	elif monnaie=="Dollars" and devise=="Euro":
		resultat=montant*2
		resultat=float(resultat)

	elif monnaie=="Euro" and devise=="Dollars":
		resultat=montant/2
		resultat=float(resultat)

	elif monnaie=="yuan" and devise=="FCFA":
		resultat=montant*88
		resultat=float(resultat)

	elif monnaie=="FCFA" and devise=="yuan":
		resultat=montant/88
		resultat=float(resultat)

	elif monnaie=="yuan" and devise=="Dollars":
		resultat=montant*0.14
		resultat=float(resultat)

	elif monnaie=="Dollars" and devise=="yuan":
		resultat=montant/0.14
		resultat=float(resultat)

	elif monnaie=="yuan" and devise=="Euro":
		resultat=montant*0.14
		resultat=float(resultat)

	elif monnaie=="Euro" and devise=="yuan":
		resultat=montant/0.14
		resultat=float(resultat)		

	else:
		print("Nous ne disposons pas de cette monnaie   ")

	decision=input(f" { resultat } " f" { devise } est la somme que vous obtiendrez après convertion. Entrez oui pour valider l'operation et non pour l'annulée   ")
	decision =str(decision)	

	if decision == "oui":
		print("Opération effectuée avec succès   ")
	elif decision == "non":
		print("Opération annulée   ")

	else:
		print("....")

	reponce = print("Voulez vous effectuez une autre convertion ?   ")
	reponce =str(reponce)

		
		




		
		


