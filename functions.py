import os


""" 
Cette fonction fait la même chose que list_of_files,
sauf qu'elle retourne le nom des fichiers
d'un repertoire donné, peu importe leur type.
Je sais pas si je la garde ou pas
"""


def name_files(directory):
    dir_list = os.listdir(directory)
    return dir_list


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


"""
Cette fonction renvoie la liste des noms de familles des présidents
"""


def list_last_names(directory):  # Fonction pas complètement opératoire, à finaliser
    L = name_files(directory)
    last_names = []
    for i in L:
        if i[-5] == '1' or i[-5] == '2':
            val = i[11:-5]
            last_names.append(val)
        else:
            val = i[11:-4]
            last_names.append(val)

    """for l in last_names:
        if last_names.count(l) >= 2:
                last_names.remove(l)"""
    return last_names


"""
Cette fonction associe à chaque nom de président son prénom
"""


def presidents(directory):
    last_names = list_last_names(directory)
    first_names = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    list_presidents = {}

    cpt = 0
    for i in first_names:
        list_presidents[i] = last_names[cpt]
        cpt += 1
    return list_presidents


"""
Cette fonction affiche les noms des différents présidents
"""


def print_names(directory):
    names = list_last_names(directory)

    for i in names:
        print(i)


"""
Cette fonction renvoie un fichier en minuscules
"""


def lowercase(text, clean_text):
    with open(text, "r") as f1, open(clean_text, "w") as f2:
        for ligne in f1:
            for i in ligne:
                if ord(i) >= 65 and ord(i) <= 90:  # Convertit les majuscules en minuscules
                    f2.write(chr(ord(i)+32))
                elif i == "\n":
                    f2.write("\n")
                else:
                    f2.write(i)

    return clean_text


"""
Cette fonction renvoie un fichier sans ponctuation
"""

def punctuation(text, clean_text):
    # clean_text = lowercase(text, 'clean_text.txt')
    with open(text, "r") as f1, open(clean_text, "w") as f2:
        for ligne in f1:
            for i in ligne:
                if (ord(i) >32 and ord(i) <= 47) and (ord(i) != 39 and ord(i) != 45):
                    f2.write('')
                elif ord(i) == 39 or ord(i) == 45:
                    f2.write(chr(32))
                else:
                    #if not (ord(i) >=32) and not (ord(i) <= 47):
                    f2.write(i)

    return #cleane_text

"""
Cette fonction calcule l'occurence de chaque mot et les stoques dans un dictionnaire 
"""
def tf(text):
    #text = punctuation(texte)

    with open(text, "r") as f1:

        d_tf = {}  #dictionnaire tf

        # transformation du texte en chaine de caractère
        chaine_mot = f1.read()
        # transformation en liste de mot
        mots = chaine_mot.split()

        # boucle parcourant la liste de mot
        for mot in mots:
            if mot:
                # Incrémentation du dictionnaire à chaque apparition de chaque mot
                d_tf[mot] = d_tf.get(mot, 0) +1

    return d_tf


"""
Cette fonction calcule le score IDF de chaque mot du text
"""
import math
def idf(directory):

    # dictionnaire qui aura pour clé chaque mot et pour valeur leur score idf
    d_idf = {}
    #  dictionnaire qui aura pour clé chaque mot et pour valeur le nombre de document dans lequel il apparait
    d_mot_par_doc = {}
    # variable indiquant le nombre de document
    nb_doc = 0

    # Boucle qui parcours chaque fichier texte dans le dossier donné (directory)
    for doc in os.listdir(directory):
        if doc.endswith(".txt"):
            with open(os.path.join(directory, doc), "r") as f:
                # stocker le contenu de chaque texte en chaine de caractère
                contenu = f.read()
                # séparation des mots
                words = contenu.split()

                for mot in words:
                    # Incrémentation du dictionnaire à l'apparition d'un mot
                    d_mot_par_doc[mot] = d_mot_par_doc.get(mot, 0) + 1

                # Incrémentation du nombre de document
                nb_doc += 1
    # boucle parcourant le dictionnaire d_mot_par_doc et calculant l'idf de chaque mot
    for mot, compteur in d_mot_par_doc.items():
        d_idf[mot] = math.log((nb_doc/compteur)+1)

    return d_idf



