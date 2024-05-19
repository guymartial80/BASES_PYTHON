try:
    # Code qui peut provoquer une exception
    result = 10 / 0
except ZeroDivisionError:
    # Code qui s'exécute si une ZeroDivisionError est levée
    print("Vous ne pouvez pas diviser par zéro.")
else:
    # Code qui s'exécute si aucune exception n'est levée
    print("La division a réussi:", result)
finally:
    # Code qui s'exécute toujours, qulque soit l'issue
    print("Bloc finalement exécuté.")