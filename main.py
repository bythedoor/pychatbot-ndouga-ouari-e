# Programme principal du projet

from functions import *


def main():  # Fonction principale, execute le programme entier

    # Affichage menu
    print("************** BIENVENUE DANS CHATBOT ! **************")
    print("\n** Menu principal - Veuillez choisir une option en tapant le numéro correspondant : \n")
    print("1 - Liste des mots les moins importants")
    print("2 - Liste des mots les plus importants")
    print("3 - Les mots les plus répétés par Chirac")
    print("4 - Liste des présidents mentionant le mot 'Nation', et celui qui le dit plus souvent")
    print("5 - Le premier président à parler d'écologie ou du climat")
    print("6 - Liste des mots que tous les présidents ont mentionné")

    # L'utilisateur choisit une des fonctionnalités, numérotées de 1 à 6
    n = 0
    while n < 0 or n > 6:
        n = int(input("Choississez un nombre >> "))

    # Un programme s'exécute en fonction de la fonctionnalité choisie
    if n == 1:  # remplacer print("0") par fonctions
        p = null_tf_idf("speeches")
        if len(p) == 0:
            print("Il n'y a pas de mots au score TF-IDF nul")
        else:
            print("Les mots non importants sont: ")
            for i in range(len(p)):
                print(p[i], end=" ")
    elif n == 2:
        p = high_tf_idf(("speeches"))
        print("Les mots importants sont: ")
        for i in range(len(p)):
            print(p[i], end=" ")
    elif n == 3:
        print(chirac("speeches"))
    elif n == 4:
        print("0")
    elif n == 5:
        print("0")
    elif n == 6:
        print("0")




if __name__ == "__main__":
    main() # on execute la fonction principale

    # tests des fonctions
    """
    n = "speeches"
    print(list_last_names(n))
    print(presidents(n))
    """
    """
    print(score_tf_idf('Nomination_Chirac1.txt', 'speeches'))
    # print(null_tf_idf())#))
    # print(idf('speeches'))
    # print(matrix_tf_idf('speeches'))
    # print(tf('Nomination_Chirac1.txt', 'speeches'))
    print(chirac('speeches'))
    # print(print_names('speeches'))
    print(presidents('speeches'))
    print(list_last_names('speeches'))
    print(list_of_files('speeches', '.txt'))
    print(lowercase('speeches'))
    print(punctuation('Nomination_Chirac1.txt', 'cleaned/clean_Chirac.txt'))
    """
    #print(lowercase('speeches'))
    #print(punctuation('cleaned'))
    #print(idf('cleaned'))
    #print(matrix_tf_idf('cleaned'))
    #print(null_tf_idf('cleaned'))
    #jf