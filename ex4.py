# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))

if 100 >= battery_level > 50:
    print((battery_level - 50) * 2 + 25 * 0.5 + 15 + (5 * 2.5) + (5 * 6), "km")

elif 50 >= battery_level > 25:
    print((battery_level - 25) * 0.5 + 15 + (5 * 2.5) + (5 * 6), "km")

elif 25 >= battery_level > 10:
    print((battery_level - 10) * 1 + (5 * 2.5) + (5 * 6), "km")

elif 10 >= battery_level > 5:
    print((battery_level - 5) * 2.5 + 5 * 6, "km")

elif 5 >= battery_level > 0:
    print(battery_level * 6, "km")

else:
    print("La batterie est vide")