def nom_fonction(paramètres_optionnels):
    """
    Documentation de la fonction (optionnelle)
    
    bloc_instructions
    """

def saluer(nom):
    """
    Salue une personne par son nom.

    Args:
        nom (str): Le nom de la personne à saluer.

    Returns:
        str: Le message de salutation.
    """
    message = f"Bonjour {nom} !"
    return message

# Appeler la fonction
personne = "Marcel"
message_salutation = saluer(personne)
print(message_salutation)  # Résultat: Bonjour Marcel !