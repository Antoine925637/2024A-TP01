# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle est la quantité d'eau à assainir? : "))


    # TODO: Doit changer pour laisser des virgules proportionnel (un chiffre après)


#Qte de "" pour 1L eau + 1 si pas un multiple de 5
nbFiltre = int(1 / 5 * water_quantity) + (water_quantity % 5 > 0)
nbLampesUV = int(3 / 5 * water_quantity) + (water_quantity % 5 > 0)
qteChlore = round(0.5 / 5 * water_quantity, 1)

print(nbFiltre, nbLampesUV, qteChlore)
