import os


""" 
Cette fonction fait la même chose que list_of_files,
sauf qu'elle retourne le nom des fichiers
d'un repertoire donné, peu importe leur type.
"""

def nom_fichiers(directory):
    dir_list = os.listdir(directory)
    return dir_list

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
                    f2.write(chr(ord(i + 32)))
                elif i == "\n":
                    f2.write("\n")
                else:
                    f2.write(i)

    return(clean_text)

