# [expression for element in iterable]

# Creation d'un dictionnaire à partir d'une liste
prenoms = ['Jean', 'Marcel', 'Emile', 'Marie']

# Creation d'un dictionnaire  depuis cette liste
dict_prenom = {k:v for k, v in enumerate(prenoms)}
print(dict_prenom)