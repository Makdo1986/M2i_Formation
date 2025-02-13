# Charger un dictionnaire
print("")
mon_dictionnaire = {"Amada" : 28, "Matthieu" : 38, "Elsa" : 5, "Bernard" : 54}

# Récupérer les données
print("")
print(f"Données du dico : {mon_dictionnaire}")
print(f"Données du dico pour la clé \"Amanda\" : {mon_dictionnaire['Amada']}")
print(f"Données du dico pour la clé \"Elsa\" : {mon_dictionnaire['Elsa']}")
print(f"Données du dico \"clé\" : {mon_dictionnaire.keys()}")
print(f"Données du dico \"values\" : {mon_dictionnaire.values()}")

# Ecraser une valeur, on indique la nomdico[clé] = value
print("")
mon_dictionnaire["Matthieu"] = 999999999
print(f"Données du dico pour la clé \"Matthieu\" : {mon_dictionnaire['Matthieu']}")
# créer un nouvel ensemble "clé/valeur" si la clé n'existe pas.
mon_dictionnaire["Michel"] = 444
print(f"Données du dico pour la clé \"Michel\" : {mon_dictionnaire['Michel']}")
print(f"Données du dico mis à jour : {mon_dictionnaire}")


# Parcourir les clés et valeurs d'un dico
# x => pour les clés
# y => pour les valeurs
print("")
for x, y in mon_dictionnaire.items():
    print(f"clé / valeur => {x} / {y}")

# Supprimer un ensemble clé / valeur
print("")
recup_value = mon_dictionnaire.pop("Matthieu")
print(f"Suppression de l'ensemble lié à la clé \"Matthieu\" : mon_dictionnaire.pop(\"Matthieu\")")
print(f"Données du dico mis à jour : {mon_dictionnaire}")
recup_value = mon_dictionnaire.popitem()
print(f"Suppression du dernier ensemble : mon_dictionnaire.popitem()")
print(f"Données du dico mis à jour : {mon_dictionnaire}")

# Fusion de dico => dico_a.update(dico_b)
print("")
mon_dictionnaire_bis = {"Jackie" : 64, "Patrick" : 62}
mon_dictionnaire.update(mon_dictionnaire_bis)
print(f"Données du dico bis : {mon_dictionnaire_bis}")
print(f"Fusion de dictionnaire  via : mon_dictionnaire.update(mon_dictionnaire_bis)")
print(f"Données du dico mis à jour : {mon_dictionnaire}")

### Créer un annuaire de personne
# Création des dictionnaires
personne_01 = {
    "Prénom" : "Matthieu",
    "Nom" : "DEGRAEVE",
    "Âge" : 38
}
personne_02 = {
    "Prénom" : "Michel",
    "Nom" : "DEGRAEVE",
    "Âge" : 72
}
personne_03 = {
    "Prénom" : "Patrick",
    "Nom" : "BAERT",
    "Âge" : 64
}
personne_04 = {
    "Prénom" : "Gabriel",
    "Nom" : "DEGRAEVE",
    "Âge" : 7
}
# Création de l'annuaire :
annuaire = [personne_01, personne_02, personne_04, personne_03]
# Boucle sur l'annuaire pour afficher les données des personnes :
print("")
for personne in annuaire:
    print(f"Entrée de l'annuaire n° {annuaire.index(personne)}")
    for categorie, donnee in personne.items():
        print(f"{categorie} : {donnee}")