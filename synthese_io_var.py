# Dans ce programe, nous allons calculer le montant TTC d'un morceau de savon.
# Il sera demander au caissier de renseigner le prix unitaire de l'article
# automatiquement le montant TTC sera calculé sachant que le taux tva est de 20%

puht = input("Saisir le prix unitaire de l'article : ")

# Conversion du type de variable puht car en l'état, c'est une chaine de caractères
puht = float(puht)

# Calcul du pttc
tva = 0.20
pttc = puht * (1 + tva)

# Affichage du montant calculé
print("Le montant de cet article est de : ", str(pttc) + " F")