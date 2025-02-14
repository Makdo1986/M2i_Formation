# # Charger un dictionnaire
# print("")
# mon_dictionnaire = {"Amada" : 28, "Matthieu" : 38, "Elsa" : 5, "Bernard" : 54}

# # Récupérer les données
# print("")
# print(f"Données du dico : {mon_dictionnaire}")
# print(f"Données du dico pour la clé \"Amanda\" : {mon_dictionnaire['Amada']}")
# print(f"Données du dico pour la clé \"Elsa\" : {mon_dictionnaire['Elsa']}")
# print(f"Données du dico \"clé\" : {mon_dictionnaire.keys()}")
# print(f"Données du dico \"values\" : {mon_dictionnaire.values()}")

# # Ecraser une valeur, on indique la nomdico[clé] = value
# print("")
# mon_dictionnaire["Matthieu"] = 999999999
# print(f"Données du dico pour la clé \"Matthieu\" : {mon_dictionnaire['Matthieu']}")
# # créer un nouvel ensemble "clé/valeur" si la clé n'existe pas.
# mon_dictionnaire["Michel"] = 444
# print(f"Données du dico pour la clé \"Michel\" : {mon_dictionnaire['Michel']}")
# print(f"Données du dico mis à jour : {mon_dictionnaire}")


# # Parcourir les clés et valeurs d'un dico
# # x => pour les clés
# # y => pour les valeurs
# print("")
# for x, y in mon_dictionnaire.items():
#     print(f"clé / valeur => {x} / {y}")

# # Supprimer un ensemble clé / valeur
# print("")
# recup_value = mon_dictionnaire.pop("Matthieu")
# print(f"Suppression de l'ensemble lié à la clé \"Matthieu\" : mon_dictionnaire.pop(\"Matthieu\")")
# print(f"Données du dico mis à jour : {mon_dictionnaire}")
# recup_value = mon_dictionnaire.popitem()
# print(f"Suppression du dernier ensemble : mon_dictionnaire.popitem()")
# print(f"Données du dico mis à jour : {mon_dictionnaire}")

# # Fusion de dico => dico_a.update(dico_b)
# print("")
# mon_dictionnaire_bis = {"Jackie" : 64, "Patrick" : 62}
# mon_dictionnaire.update(mon_dictionnaire_bis)
# print(f"Données du dico bis : {mon_dictionnaire_bis}")
# print(f"Fusion de dictionnaire  via : mon_dictionnaire.update(mon_dictionnaire_bis)")
# print(f"Données du dico mis à jour : {mon_dictionnaire}")

# ### Créer un annuaire de personne
# # Création des dictionnaires
# personne_01 = {
#     "Prénom" : "Matthieu",
#     "Nom" : "DEGRAEVE",
#     "Âge" : 38
# }
# personne_02 = {
#     "Prénom" : "Michel",
#     "Nom" : "DEGRAEVE",
#     "Âge" : 72
# }
# personne_03 = {
#     "Prénom" : "Patrick",
#     "Nom" : "BAERT",
#     "Âge" : 64
# }
# personne_04 = {
#     "Prénom" : "Gabriel",
#     "Nom" : "DEGRAEVE",
#     "Âge" : 7
# }
# # Création de l'annuaire :
# annuaire = [personne_01, personne_02, personne_04, personne_03]
# # Boucle sur l'annuaire pour afficher les données des personnes :
# print("")
# for personne in annuaire:
#     print(f"Entrée de l'annuaire n° {annuaire.index(personne)}")
#     for categorie, donnee in personne.items():
#         print(f"{categorie} : {donnee}")

# Exo 01

# Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec :
# - désignation
# - numéro de voie
# - complément
# - intitulé de voie
# - commune
# - code postal
# Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire.
# Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur.

annuaire_adresse = {}

def gestion_annuaire_adresse():
    pass

def ajout_adresse(annuaire):
    print("Ajout d'une adresse, veuillez saisir :")
    designation = input("- sa désignation : ")
    numero = input("- son numéro : ")
    complement = input("- son complément : ")
    intitule = input("- son intitulé de voie : ")
    commune = input("- sa commune : ")
    code_postal = input("- son code postal : ")
    adresse = { 
        "Numéro" : numero, 
        "Complément" : complement,
        "Intitulé" : intitule,
        "Commune" : commune,
        "Code Postal" : code_postal,
    }
    annuaire[designation] = adresse

def edition_adresse():
    pass

def suppression_adresse():
    pass

def affichage_adresse(annuaire):
    for designation, adresse in annuaire.items():
        print(f"Annuaire d'adresse référencé : {designation}")
        for categorie, donnee in adresse.items():
            print("-", categorie, "=>", donnee)

# Essai saisie d'une adresse :
#|# ajout_adresse(annuaire_adresse)

annuaire_adresse_demo = {
    "Matthieu" :
        {    
        "Numéro" : "37", 
        "Complément" : "",
        "Intitulé" : "rue coppens",
        "Commune" : "Hondschoote",
        "Code Postal" : "59122",
        },
    "Dominique" :
        {    
        "Numéro" : "11", 
        "Complément" : "",
        "Intitulé" : "rue notre damde",
        "Commune" : "Hazebrouck",
        "Code Postal" : "59190",
        }
        ,
    "Elodie" :
        {    
        "Numéro" : "666", 
        "Complément" : "Grange",
        "Intitulé" : "rue sébastopol",
        "Commune" : "Boeschepe",
        "Code Postal" : "59299",
        }
}

affichage_adresse(annuaire_adresse_demo)