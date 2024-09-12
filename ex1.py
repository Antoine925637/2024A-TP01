# TODO: Créer un script permettant le formattage du livre des records des JO.

#Collecte des données
country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
sport = input("Dans quelle discipline ? ")
category = input("Dans une catégorie spécifique ? ")
record = input("Quel est le record ? ")

#Afficher les données
print("\nNouveau Record:")
print("--------------------")
print(date,"-", sport,"-", category+":")
print("\t"+athlete,"("+country+")","-",record)