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
        else:
            val = i[11:-4]
        if val not in last_names:
            last_names.append(val)

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
def lowercase(directory):

    # Créer le répertoire "cleaned" s'il n'existe pas
    cleaned_directory = os.path.join(os.getcwd(), "cleaned")
    if not os.path.exists(cleaned_directory):
        os.makedirs(cleaned_directory)

    l_files = list_of_files(directory, '.txt')
    l_nom = list_last_names(directory)

    for doc in os.listdir(directory):
        if doc.endswith(".txt"):
            p_nom = ""
            for nom in l_nom:
                if nom in doc:
                    p_nom = nom

            #clean_text = os.rename(doc, 'clean_'+p_nom)
            input = os.path.join(directory,doc)
            output = os.path.join(cleaned_directory, doc.replace(".txt", "_clean.txt"))

            with open(input, "r") as f1, open(output, "w") as f2:

                for ligne in f1:
                    for i in ligne:
                        if ord(i) >= 65 and ord(i) <= 90:  # Convertit les majuscules en minuscules
                            f2.write(chr(ord(i)+32))
                        elif i == "\n":
                            f2.write("\n")
                        else:
                            f2.write(i)
                #punctuation(f1,f2)
        #n_nom = 'clean_'+p_nom+'.txt'
        #os.rename(os.path.join(cleaned_directory, doc), os.path.join(cleaned_directory, n_nom))
    return #clean_text

"""
Cette fonction transforme tous les fichiers d'un repertoire sans ponctuation
"""

def punctuation(directory):
    # clean_text = lowercase(text, 'clean_text.txt')

    for text in os.listdir(directory):
        if text.endswith(".txt"):
            with open(os.path.join(directory, text), "r", encoding = 'UTF-8') as f1:

                t_clean = ""
                for ligne in f1:
                    for i in ligne:
                        if (ord(i) >32 and ord(i) <= 47) and (ord(i) != 39 and ord(i) != 45):
                            t_clean += ''
                        elif ord(i) == 39 or ord(i) == 45:
                            t_clean += chr(32)
                        else:
                            #if not (ord(i) >=32) and not (ord(i) <= 47):
                            t_clean += i

            with open(os.path.join(directory,text), 'w', encoding = 'UTF-8') as f2:
                f2.write(t_clean)

    return

"""
Cette fonction calcule l'occurence de chaque mot et les stockes dans un dictionnaire 
"""
def tf(text, directory):
    #text = punctuation(texte)

    with open(os.path.join(directory,text), "r", encoding = 'UTF-8') as f1:

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
            with open(os.path.join(directory, doc), "r", encoding = 'UTF-8') as f:
                # stocker le contenu de chaque texte en chaine de caractère
                contenu = f.read()
                # séparation des mots
                words = contenu.split()

                d_tf = tf(doc, directory)
                # for mot in words:

                # print(d_tf)

                for mot in d_tf.keys():
                    if mot in d_mot_par_doc.keys():
                        d_mot_par_doc[mot] += 1
                    else:
                        d_mot_par_doc[mot] = 1
                """
                for mot in words:
                    # Incrémentation du dictionnaire à l'apparition d'un mot
                    d_mot_par_doc[mot] = d_mot_par_doc.get(mot, 0) + 1
                """
                # Incrémentation du nombre de document
                nb_doc += 1
    # boucle parcourant le dictionnaire d_mot_par_doc et calculant l'idf de chaque mot
    for mot, compteur in d_mot_par_doc.items():
        d_idf[mot] = round(math.log10((nb_doc/compteur)),2)

    return d_idf

"""
Cette fonction calcule le score TF-IDF de chaque mot d'un text
"""
def score_tf_idf_text(text, directory):
    # dictionnaire qui stoquera les score tf-idf de chaque mot d'un document
    d_tf_idf_text = {}
    # appel du dictionnaire IDF
    d_idf = idf(directory)
    # appel du dictionnaire TF du document en question
    d_tf = tf(text, directory)
    # Boucle qui Incrémente le dictionnaire avec les scores TF-IDF en faisant TF * IDF
    for word, count in d_tf.items():
        if word not in d_tf_idf_text:
            d_tf_idf_text[word] = count * d_idf.get(word, 0)
        """
        else:
            d_tf_idf_text[word] += count * d_idf.get(word, 0)
        """
    return d_tf_idf_text



"""
Cette fonction calcule le score TF-IDF de chaque mot du repertoire
"""
"""
def score_tf_idf(directory):

    # dictionnaire qui stoquera les score tf-idf de chaque mot d'un document
    d_tf_idf = {}
    # appel du dictionnaire IDF
    d_idf = idf(directory)

    for doc in os.listdir(directory):
        if doc.endswith(".txt"):
            #with open(os.path.join(directory, doc), "r") as f:

            # appel du dictionnaire TF du document en question
            d_tf = tf(doc, directory)

            # Boucle qui Incrémente le dictionnaire avec les scores TF-IDF en faisant TF * IDF
            for word, count in d_tf.items():
                if word not in d_tf_idf:
                    d_tf_idf[word] = count * d_idf.get(word, 0)
                else:
                    d_tf_idf[word] += count * d_idf.get(word, 0)

    return d_tf_idf
"""

"""
Cette fonction renvoie la matrice TF-IDF
"""

def matrix_tf_idf(directory):
    # Création de la matrice contenant par ligne le score TF-IDF d'un mot dans chaqu'un des textes, une colonne représente un fichier texte
    matrix_tf_idf = {}
    # appel du dictionnaire IDF
    d_idf = idf(directory)
    # appel du dictionnaire donnant le score TF-IDF de chaque mot
    #d_tf_idf = score_tf_idf(directory)

    # Boucle parcourant chaque mot (clé) dans le dictionnaire idf
    for word in d_idf.keys():
        # Création d'une liste correspondant au score TF-IDF d'un même mots dans chaque document
        l_mot_par_doc = []
        # Boucle parcourant chaque document
        for doc in os.listdir(directory):

            if doc.endswith(".txt"):
                #with open(os.path.join(directory, doc), "r") as f:
                    #chaine = f.read()

                #d_tf = tf(doc, directory)

                d_tf_idf_text = score_tf_idf_text(doc, directory)
                # Incrémentation de la ligne avec le score TF-IDF du mot s'il se trouve dans le document (doc)
                if word in d_tf_idf_text:
                    l_mot_par_doc.append(d_tf_idf_text[word])
                else: # sinon donner une valeur de 0
                    l_mot_par_doc.append(0)


        # Ajout de chaque ligne (liste) dans la matrice
        matrix_tf_idf[word] = l_mot_par_doc

    return matrix_tf_idf



"""
Cette fonction renvoie la liste des mots dont le score TD-IDF est nul
"""

def null_tf_idf(directory):
    #L = list_of_files(directory, '.txt')
    matrice = matrix_tf_idf('cleaned')
    mot_score_nul = []
    for mot, scores in matrice.items():
        nul = True
        for score in scores:
            if score != 0.0:
                nul = False
        if nul:
            mot_score_nul.append(mot)

    return mot_score_nul, len(mot_score_nul)


"""
Cette fonction renvoie la liste des mots avec le score TD-IF le plus élevé
"""

def high_tf_idf(directory):
    L = name_files(directory)
    M = []
    max = 0
    for i in L:
        dico = (score_tf_idf_text(i, directory))
        for item in dico.items():
            if item[1] > max:
                max = item[1]
        for item in dico.items():
            if item[1] == max :
                M.append(item[0])
    return M



def chirac(directory):
    # variable qui contiendra le/les mots les plus répété(s)
    mot_plus_repete = ""
    # Variable qui stoquera l'occurence du/des mots le/les plus utilisé(s)
    occ = 0

    # Boucle qui parcours les documents dans lesquel le mot "Chirac" apparait
    for doc in os.listdir(directory):
        if doc.endswith(".txt") and "Chirac" in doc:
            with open(os.path.join(directory, doc), "r") as f:
                # appel du dicyionnaire TF du document en question (doc)
                d_tf = tf(doc, directory)

                # Bouble qui parcours le dictionnaire TF et qui compare les valeurs des occurences
                for word, count in d_tf.items():
                    if count > occ:
                        occ = count
                        mot_plus_repete = word
                    elif count == occ:
                        mot_plus_repete += ", " + word
    #jf
    # Création de la phrase réponse
    phrase = "Le(s) mot(s) le(s) plus répété(s) est/sont '" + mot_plus_repete + "'"

    return phrase


def nation():
    L = name_files("speeches")
    M = []

    cpt = 0
    for i in L:
        with open(i, "r") as f1:
            for ligne in f1:
                if "nation" in ligne:
                    cpt += 1
            f1.close()
            if cpt > 0:
                M.append(i)
    return M


def ecology(directory):
    L = name_files(directory)
    M = []
    eco = True
    for i in L:
        dico = (score_tf_idf_text(i, directory))
        for item in dico.items():
            if item[0] == "ecologie" and eco:
                M.append(i)
    return M


def token_question(question):
    q_clean = ""
    L = []  # Initialisation des variables

    for i in question: # Cette boucle fait l'addition des caract

        if ord(i) >= 65 and ord(i) <= 90: #
            q_clean += (chr(ord(i) + 32))

        elif (ord(i) > 32 and ord(i) <= 47) and (ord(i) != 39 and ord(i) != 45):
            q_clean += ''

        elif ord(i) == 39 or ord(i) == 45 or ord(i) == 63:
            q_clean += chr(32)

        else:
            q_clean += i

    L = q_clean.split()
    return L


def intersection(q_token, directory):
    L = []
    dico = matrix_tf_idf(directory)

    for i in dico.keys():
        if i in q_token:
            L.append(i)

    return L


