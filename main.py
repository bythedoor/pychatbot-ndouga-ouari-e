# Programme principal du projet

from functions import *


def main():  # Fonction principale, execute le programme entier

    # Affichage menu
    print("************** BIENVENUE DANS CHATBOT ! **************")
    print("\n** Menu principal - Veuillez choisir une option en tapant le numéro correspondant : \n")
    print("1 - Liste des mots les moins importants")
    print("2 - Liste des mots les plus importants")
    print("3 - Les mots les plus répétés par Chirac")
    print("4 - Liste des présidents mentionnant le mot 'Nation', et celui qui le dit plus souvent")
    print("5 - Liste des présidents qui ont parlé d'écologie ou du climat")

    # L'utilisateur choisit une des fonctionnalités, numérotées de 1 à 6
    n = -1
    while n < 0 or n > 6:
        n = int(input("Choississez un nombre >> "))

    # Un programme s'exécute en fonction de la fonctionnalité choisie
    if n == 1:
        # on initialise une variable avec la liste des mots les moins utilisés
        p = null_tf_idf("speeches")

        # s'il n'y a aucun mot dans la liste, on le signale à l'utilisateur
        if len(p) == 0:
            print("Il n'y a pas de mots au score TF-IDF nul")

        # on affiche les mots les moins utilisés séparés par un espace
        else:
            print("Les mots non importants sont: ")
            for i in range(len(p)):
                print(p[i], end=" ")

    elif n == 2:
        # on initialise une variable avec la liste des mots les plus utilisés
        p = high_tf_idf(("cleaned"))

        # s'il n'y a aucun mot dans la liste, on le signale à l'utilisateur
        if len(p) == 0:
            print("Il n'y a pas de mots au score TF-IDF nul")

        # on affiche les mots les plus utilisés séparés par un espace
        else:
            print("Les mots importants sont: ")
            for i in p:
                print(i, end=" - ")

    elif n == 3:
        print(chirac("speeches"))

    elif n == 4:
        print(mot_dit("nation"))

    elif n == 5:
        print("0")

# tests
print(score_tf_idf_text("Nomination_Chirac1_clean.txt", "cleaned"))
t = score_tf_idf_text("Nomination_Chirac1_clean.txt", "cleaned")
print(list(t.values()))