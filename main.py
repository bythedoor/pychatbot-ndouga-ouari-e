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
    #print("6 - Liste des mots que tous les présidents ont mentionné")

    # L'utilisateur choisit une des fonctionnalités, numérotées de 1 à 6
    n = 0
    while n < 0 or n > 6:
        n = int(input("Choississez un nombre >> "))

    # Un programme s'exécute en fonction de la fonctionnalité choisie
    if n == 1:  # remplacer print("0") par fonctions
        p = null_tf_idf("cleaned")
        if len(p) == 0:
            print("Il n'y a pas de mots au score TF-IDF nul")

        # on affiche les mots les moins utilisés séparés par un espace
        else:
            print("Les mots non importants sont: ")
            for i in p:
                print(p[i], end=" ,")
    elif n == 2:
        # on initialise une variable avec la liste des mots les plus utilisés
        p = high_tf_idf(("cleaned"))
        print("Les mots importants sont: ", end=" ")
        for i in range(len(p)):
            print(p[i], end=" ,")
    elif n == 3:
        print(chirac("cleaned"))

    elif n == 4: # liste des présidents qui on dit le mot 'nation'
        p = mot_dit('nation')
        print("Les présidents qui ont dit le mot 'nation' sont", end=" ")
        cpt = 0
        for i in p:
            if cpt == len(p):
                print("et ", i, end=".")
            else:
                print(i, end=", ")
            cpt += 1

    elif n == 5:
        ecologie = mot_dit('ecologie')
        climat = mot_dit('climat')
        print("Le président qui ont dit le parle de climat et d'écologie est", end=" ")
        for i in ecologie:
            climat.add(i)
        final = set(climat)

        cpt = 0
        for i in final:
            if cpt == len(final):
                print("et ", i, end=".")
            else:
                print(i, end=", ")
            cpt += 1
    #elif n == 6:
    #    print("0")


# tests
print(score_tf_idf_text("Nomination_Chirac1_clean.txt", "cleaned"))
t = score_tf_idf_text("Nomination_Chirac1_clean.txt", "cleaned")
print(list(t.values()))


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
    #print(chirac('cleaned'))
    #print(high_tf_idf('cleaned'))
    #print(mot_dit("nation"))
    #print(list_last_names('cleaned'))
    #print(presidents('cleaned'))
    #print(print_names('speeches'))
    #print(tf_idf_token('de quoi ca parle'))
    #print(create_tfidf_matrix_optimized('cleaned'))
    #print(score_tf_idf_text('Nomination_Chirac1_clean.txt', 'cleaned'))
    print(matrix_tf_idf_2('cleaned'))
    print(tf_idf_token('la responsabilité qu ils m ont confiée est un honneur dont je mesure la gravité'))
    print(pertinent_document(matrix_tf_idf_2('cleaned'), tf_idf_token('la responsabilité qu ils m ont confiée est un honneur dont je mesure la gravité'), name_files('cleaned')))
    print(generate_answer("responsabilité qu ils m ont confiée est un honneur dont je mesure la gravité"))