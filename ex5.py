#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.
from itertools import count

gold = silver = bronze = 0
country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
if set(code_medals) != {'G','S','B'}:
    print("Ceci est une chaine invalide.")
else:
    gold = code_medals.count("G")
    silver = code_medals.count("S")
    bronze = code_medals.count("B")

    print(country+":")
    print("-",gold,"Or")
    print("-",silver,"Argent")
    print("-",bronze,"Bronze")