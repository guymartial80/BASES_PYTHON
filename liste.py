# Création et affichage d'une liste
pair = [2, 4, 6, 8, 10, 12]
print(pair)

# Affichage de la longueur d'une liste
pair = [2, 4, 6, 8, 10, 12]
print(len(pair))

# Affichage des valeurs comprises entre le 2ème et 5ème élément de la liste
pair = [2, 4, 6, 8, 10, 12]
print(pair[1:4])

# Suppression de l'élément "4" dans la liste et affichage du résultat
pair = [2, 4, 6, 8, 10, 12]
pair.remove(4)
print(pair)

# Suppression du troisième élément de la liste et affichage du résultat
pair = [2, 4, 6, 18, 8, 10, 12]
pair.pop(2)
print(pair)

# tri par ordre croissant des éléments de type numérique de la liste et affichage du résultat
pair = [2, 4, 6, 18, 8, 10, 12]
pair.sort()
print(pair)

# tri par ordre alphabétique (croissant) des éléments de type chaine de caractères de la liste et affichage du résultat
lettres = ["b", "r", "e", "t", "o"]
lettres.sort()
print(lettres)
