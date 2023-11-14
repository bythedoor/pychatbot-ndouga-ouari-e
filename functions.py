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
def list_last_names(directory):
    L = name_files(directory)
    last_names = []
    for i in L:
        if i[-5] == '1' or i[-5] == '2':
            val = i[11:-5]
            last_names.append(val)
        else:
            val = i[11:-4]
            last_names.append(val)

    for l in last_names:
        if last_names.count(l) >= 2:
                last_names.remove(l)
    return last_names

"""
Cette fonction associe à chaque nom de président son prénom
"""

def presidents(directory):
    last_names = list_last_names(directory)
    first_names = ["Jacques", "Valéry","François","Emmanuel","François","Nicolas"]
    list_presidents = {}

    cpt = 0
    for i in first_names:
        list_presidents[i] = last_names[cpt]
        cpt += 1
    return  list_presidents

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

def punctuation(text, clean_text):
    #clean = lowercase(text)
    with open(text, "r") as f1, open(clean_text, "w") as f2:
        for ligne in f1:
            for i in ligne:
                if ord(i) >32 and ord(i) <= 47:
                    f2.write('')
                elif ord(i) == 44 or ord(i) == 45:
                    f2.write(chr(32))
                else:
                    #if not (ord(i) >=32) and not (ord(i) <= 47):
                    f2.write(i)

    return #(cleane_text)

"""
Cette fonction calcule l'occurences d'un mot 
"""
def occurence(word, text):
    #text = punctuation(texte)

    with open(text, "r") as f1:
        tf = 0  # score tf
        for ligne in f1:
            mot = ""
            for i in ligne:
                if ord(i) >=  97 and ord(i) <= 122:
                    mot += i
                elif ord(i) == 32:
                    if mot == word:
                        tf += 1
                    mot = ""
    return tf
