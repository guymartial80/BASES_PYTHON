prix_fruits = {'orange' : 150, 'papaye' : 200, 'mangue' : 300}
# print(prix_fruits)


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

print(len(prix_fruits))

prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

print(prix_fruits['orange'])


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}
premiers_fruits = list(prix_fruits.items())[:2]
print(premiers_fruits)


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

# Affichage du prix d'un tas de mangues
print('Prix tas de mangues : ', prix_fruits['mangue'])


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

print( prix_fruits.keys())


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

print( prix_fruits.values())



prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

print( prix_fruits.items())


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

prix_fruits['ananas'] = 500
print(prix_fruits)


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300, 
               'ananas' : 500}

print(prix_fruits)
prix_fruits.pop('mangue')
print(prix_fruits)
del prix_fruits['papaye']
print(prix_fruits)


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300}

prix_fruits['orange'] = 350
print(prix_fruits)


prix_fruits = {'orange' : 150, 
               'papaye' : 200, 
               'mangue' : 300, 
               'citron' : 100, 
               'pomme' : 400, 
               'fraise' : 600, 
               'piment' : 180}

selection_fruits = list(prix_fruits.items())[2:5]
print(selection_fruits)