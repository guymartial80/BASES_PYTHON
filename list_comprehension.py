
# [expression for element in iterable if condition]


nombres = [1, 2, 3, 4, 5]
# Créer une liste des carrés des nombres pairs
carres_pairs = [nombre * nombre for nombre in nombres if nombre % 2 == 0]
print(carres_pairs)

nombre_1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]
# Créer une liste des carrés des nombres pairs
result_carres = [nombre **2 for nombre in nombre_1 if nombre % 2 != 0]
print(result_carres)
