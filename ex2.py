# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))

nbFiltre = str(int(1 / 5 * water_quantity))
nbLampesUV = str(int(3 / 5 * water_quantity))
qteChlore = str(round(0.5 / 5 * water_quantity, 1))

print("Voici les éléments requis pour assainir", str(water_quantity) + "L d'eau:\n" + "\t- Filtre(s) :", nbFiltre + "\n" + "\t- Lampe(s) UV :", nbLampesUV + "\n" + "\t- Chlore :", qteChlore + "kg")
