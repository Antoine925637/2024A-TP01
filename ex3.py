# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math
from math import radians

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))
distance = round(((speed**2*math.sin(2*radians(angle)))/9.8),2)
print("Distance parcourue:",str(distance)+"m")
