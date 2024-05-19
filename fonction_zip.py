# Liste de prénoms d'étudiants
etudiants = ['Jean', 'Marcel', 'Emile', 'Marie', 'Georges']

# Liste de notes des étudiants
notes = [12, 14, 11, 18, 13]

# utilisation de la fonction zip
notes_etudiants = {etudiant:note for etudiant, note in zip(etudiants, notes) if note > 12}
print(notes_etudiants)
