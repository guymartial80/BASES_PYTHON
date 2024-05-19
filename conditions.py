age = 18

if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")



note = 75

if note >= 90:
    print("Excellent !")
elif note >= 80:
    print("Très bien !")
elif note >= 65:
    print("Bien !")
else:
    print("Insuffisant.")


semaine = "dimanche"
a_plu = True
est_midi = 12

if semaine == "dimanche" or a_plu or est_midi:
    print("Je peux rester à la maison.")
else:
    print("Je dois aller travailler.")


age = 17
est_etudiant = True

if not (age >= 18 and est_etudiant):
    print("Vous ne pouvez pas bénéficier de la bourse d'études.")
else:
    print("Vous pouvez bénéficier de la bourse d'études.")

    
age = 17
a_obtenu_bac = True
est_camerounais = True

if (age >= 17 and a_obtenu_bac) and est_camerounais:
    print("Bienvenue à l\'Université!")
else:
    print("Une des conditions n\'est pas respectée")



fruits = ["pomme", "banane", "orange", "mangue"]
choix_fruit = input("Quel fruit voulez-vous ? (pomme, banane, orange, mangue) : ")

if choix_fruit.lower() in fruits:  
  print(f"Vous avez choisi une {choix_fruit}.")
else:
  print(f"Le fruit '{choix_fruit}' n'est pas disponible dans notre stock.")