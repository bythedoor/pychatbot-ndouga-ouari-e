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

def list_last_names(directory):
    L = name_files(directory)
    last_names = []
    M = "Nomination_.txt12"
    for i in L:
        val = i - M
        last_names.append(val)
    return last_names


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


"""
Cette fonction associe à chaque nom de président son prénom
"""

def presidents(last_names):
    list_presidents = {}
    first_names = []

    cpt = 0
    for i in first_names:
        list_presidents[i] = last_names[cpt]
        cpt += 1

"""
Cette fonction affiche les noms des différents présidents
"""
def print_names(names):
    cpt = 0

    for i in names:
        for j in range(len(names)):
            if names[j] == i:
                cpt += 1
        if cpt > 1:
            print(i, end=" ")

    print()

"""
Cette fonction renvoie un fichier en minuscules
"""
def lowercase(text, clean_text):
    with open(text, "r") as f1, open(clean_text, "w") as f2:
        for ligne in f1:
            for i in ligne:
                if ord(i) >= 65 and ord(i) <= 90:
                    f2.write(chr(ord(i)+32))
                elif i == "\n":
                    f2.write("\n")
                else:
                    f2.write(i)

    return(clean_text)


"""
Cette fonction renvoie un fichier sans ponctiation
"""

def punctuation(text):
    clean = lowercase(text)
    with open(clean, "r") as f1, open(clean_text, "w") as f2:
        for ligne in f1:
            for i in ligne:
                if ord(i) >= 33 and ord(i) <= 47:
                    f2.write(chr(ord()))
                if ord(i) == 44 or ord(i) == 45:
                    f2.write(chr(ord(32)))
                elif i == "\n":
                    f2.write("\n")
                else:
                    f2.write(i)

    return (cleane_text)

"""
Cette fonction calcule l'occurences d'un mot 
"""
def occurence(word, text):
    #text = punctuation(texte)
    tf = 0 # score tf
    with open(text, "r") as f1:
        for ligne in f1:
            mot = ""
            for i in ligne:
                if ord(i) >=  97 and ord(i) <= 122:
                    mot += ord(i)
                elif ord(i) == 32:
                    if mot == word:
                        tf += 1
                    mot = ""
    return tf
