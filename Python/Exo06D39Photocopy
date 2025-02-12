# Dans une reprographie, le coût des photocopies dépend de la quantité demandée :
# Pour moins de 10 copies, le prix est de 0,5 euros par copie.
# Pour un nombre de copies entre 10 et 20 inclus, le prix est de 0,4 euros par copie.
# Au-delà de 20 copies, le prix est de 0,3 euros par copie.
# 
# Écrivez un algorithme qui demande à l'utilisateur le nombre de photocopies à effectuer et qui calcule le prix à payer.

nbCopieDemande = int(input("Combien de copie voulez-vous ? [nombre entier] "))

# Calcul du prix d'une copie en fonction du nombre de copie demandé
if nbCopieDemande > 20 :
    prixCopie = 0.3
elif nbCopieDemande > 9 :
    prixCopie = 0.4
else :
    prixCopie = 0.5

# Affichage du texte résultat
print(f"Pour \"{nbCopieDemande}\" copie(s) demandée(s), prix d'une copie \"{prixCopie:.2f} €\", vous aller payer {nbCopieDemande * prixCopie:.2f} €.")