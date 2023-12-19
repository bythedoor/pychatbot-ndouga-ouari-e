import os
import math

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
    # Si on recherche les nom des présidents dans le répertoire 'cleaned'
    if directory == 'cleaned':
        a = 11
        b = 10
    else:  # Sinon dans le répertoire 'speeches'
        a = 5
        b = 4
    last_names = []
    for i in L:
        if i[-a] == '1' or i[-a] == '2':
            val = i[11:-a]
        else:
            val = i[11:-b]
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
    for i in range(len(first_names)):
        prenom = first_names[i]
        list_presidents[last_names[i]] = prenom
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

    return mot_score_nul #, len(mot_score_nul)


"""
Cette fonction renvoie la liste des mots avec le score TD-IF le plus élevé
"""
# Fonction intermédaire qui récupère le maximum d'une liste
def max_list(L):
    max = 0
    for i in L:
        if i > max:
            max = i
        return max


def high_tf_idf(directory):
    L = name_files(directory)
    M = []
    max = 0
    l_mot = []
    matrice = matrix_tf_idf('cleaned')
    for mot, scores in matrice.items():

        maxi = max_list(scores)
        if maxi > max:
            max = maxi
            l_mot = []
            l_mot.append(mot)

        elif maxi == max:
            l_mot.append(mot)

    return l_mot



def chirac(directory):
    # variable qui contiendra le/les mots les plus répété(s)
    mot_plus_repete = ""
    # Variable qui stoquera l'occurence du/des mots le/les plus utilisé(s)
    occ = 0

    mot_score_nul = null_tf_idf(('cleaned'))

    # Boucle qui parcours les documents dans lesquel le mot "Chirac" apparait
    for doc in os.listdir(directory):
        if doc.endswith(".txt") and "Chirac" in doc:
            with open(os.path.join(directory, doc), "r") as f:
                # appel du dicyionnaire TF du document en question (doc)
                d_tf = tf(doc, directory)

                # Bouble qui parcours le dictionnaire TF et qui compare les valeurs des occurences
                for word, count in d_tf.items():
                    if count > occ and word not in mot_score_nul:
                        occ = count
                        mot_plus_repete = word
                    elif count == occ and word not in mot_score_nul:
                        mot_plus_repete += ", " + word

    # Création de la phrase réponse
    phrase = "Le(s) mot(s) le(s) plus répété(s) est/sont '" + mot_plus_repete + "'"

    return phrase


"""
Cette fonction renvoie la liste des présidents qui ont dis un même mot

def mot_presidents(mot):
    l_presidents = []
    list_doc = os.listdir('cleaned')

    for doc in list_doc:
"""
"""
Cette fonction renvoie les présidents qui ont parlé de nation
"""
def mot_dit(mot):
    """
    :param mot: str --> list """
    corpus = name_files('cleaned')

    matrix = matrix_tf_idf('cleaned')
    l_president = []
    nom = list_last_names("cleaned")

    cpt = 0

    for doc in corpus:
        if matrix[mot][cpt] != 0: # Si le mot est dit par un président (son tfidf est strictement différent 0)
            if ( (cpt == 1 or cpt == 6) and (matrix[mot][cpt -1] == 0) ) or ( cpt != 1 and cpt != 6):
                if cpt == 0 or cpt == 1:
                    nom_p = nom[0]
                elif cpt <= 5 and cpt >= 2 :
                    nom_p = nom[cpt - 1]
                elif cpt == 5 or cpt == 6:
                    nom_p = nom[4]
                else:
                    nom_p = nom[5]
                l_president.append(nom_p)
        cpt += 1
    d_presidents = presidents('cleaned')
    cpt = 0
    for nom in l_president: # On parcours la liste des présidents qui ont dis le mots et on ajoute leur prénom
        prenom = d_presidents[nom]
        l_president[cpt] = "{1} {0}".format(nom, prenom)
        cpt += 1

    return set(l_president)# on retourne en supprimant les doublons





"""
Cette fonction trace une matrice TF-IDF avec comme nombre de ligne le nombre de documents et comme nombre de colonne le nombre de mot
"""
def matrix_tf_idf_2(directory):
    # création de la nouvelle matrice
    matrice_tf_idf = {}
    # appel de notre dictionnaire contenant l'IDF de chaque mot
    d_idf = idf(directory)
    cpt = 1
    for doc in os.listdir(directory):
        if doc.endswith(".txt"):
            # appel de la fonction qui nous permet de calculer le score tf_idf de chaque mot d'un document
            d_tf_idf_text = score_tf_idf_text(doc, directory)
            # On parcours le dictionnaire en disant que si le mot n'est pas dans notre document actuel on l'ajoute dans le dictionnaire avec un score de 0
            for mot in d_idf.keys():
                if mot not in d_tf_idf_text:
                    d_tf_idf_text[mot] = 0
            # on ajoute à notre matrice les scores d'un texte correspondant à une ligne de la matrice
            matrice_tf_idf[cpt] = d_tf_idf_text
            cpt += 1 # incrémentation du compteur

    return matrice_tf_idf



def token_question(question):
    q_clean = ""

    # création du token de chaque mot de la question
    for i in question:

        # convertit les majuscules en minuscules
        if ord(i) >= 65 and ord(i) <= 90:
            q_clean += (chr(ord(i) + 32))

        # convertit les caractères spéciaux en espace
        elif (ord(i) > 32 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64):
            q_clean += ' '

        # si le caractère n'est ni une majuscule, ni un caractère spécial, on le garde dans le token
        else:
            q_clean += i

    L = q_clean.split()  # sépare les différents mots de la question
    return L


def intersection(q_token, directory):
    L = []
    dico = matrix_tf_idf(directory)

    # la boucle vérifie si chaque token de la question apparait dans le corpus
    for i in dico.keys():

        # si le token est parmi les clés du dictionnaire tf-idf, on l'ajoute dans une liste
        if i in q_token:
            L.append(i)

    # on renvoie la liste des mots de la question qui sont également dans le corpus
    return L


"""
Cette fonction calcume le produit scalaire de 2 vecteurs
"""
def scalaire(vector1, vector2):
    """
    :param vector1: list
    :param vector2: list
    :return: float
    """
    r = 0
    for a, b in zip(vector1, vector2): # on parcourt nos vecteur
        r += a*b # somme du produit des valeurs des vecteur
    return r

def norme_vecteur(a):
    s = 0

    for i in a:
        s += i**2

    norme = math.sqrt(s)

    return norme

"""
Cette fonction calcule le score de similarité de deux vecteurs a et b
"""
def similiarite(a, b):
    """
    :param a: list
    :param b: list
    :return: float
    """
    score = scalaire(a,b)/(norme_vecteur(a) * norme_vecteur(b))
    return score




"""
Calcule le score tf-idf de chaque mot d'une question
"""

def tf_idf_token(question_words):

    idf_scores = idf('cleaned')
    corpus_directory = 'cleaned'

    word_indices = {word: index for index, word in enumerate(idf_scores)}

    # Initialiser le vecteur TF-IDF de la question avec des zéros
    tfidf_vector = [0] * len(idf_scores)

    # création du dictionnaire TF
    tf_scores = {}
    for word in question_words:
        tf_scores[word] = tf_scores.get(word, 0) + 1 # Calcul du le score TF pour chaque mot dans la question

    # Calcul du vecteur TF-IDF de la question
    for word, tf_score in tf_scores.items():
        if word in word_indices:
            # Obtenir l'indice du mot dans le vecteur TF-IDF
            word_index = word_indices[word]
            # Calcul du score TF-IDF
            tfidf_vector[word_index] = tf_score * idf_scores[word]

    return tfidf_vector


"""
Cette fonction calcume le produit scalaire de 2 vecteurs
"""
def scalaire(vector1, vector2):
    """
    :param vector1: list
    :param vector2: list
    :return: float
    """
    r = 0
    for a, b in zip(vector1, vector2): # on parcourt nos vecteur
        r += a*b # somme du produit des valeurs des vecteur
    return r



"""
Cette fonction renvoie le mot avec le score TD-IDF le plus élévé
"""
def high_tf_idf_token(a, q_token):
    max = a[0]

    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]

    doc = pertinence()
    # with open()

    return max


"""
Cette fonction cherche le document le plus pertinent en fonction d'une question
"""
def pertinent_document(matrix_tf_idf, tf_idf_question, file_names):
    """
    :param matrix_tf_idf: dict
    :param tf_idf_question: list
    :param file_names: list
    :return: int
    """
    # création d'une liste qui contiendra des tuples avec pour indice 0 le numéro du document et pour indice 1 sa similarité de la question avec le texte
    similarities = []
    # on parcourt notre matrice en calculant la similarité de la question avec chaque document
    for file_name, tf_idf_document in matrix_tf_idf.items():
        similarity = similiarite(tf_idf_question, tf_idf_document.values())
        # Ajout du tuple (nom du fichier, similarité) à la liste
        similarities.append((file_name, similarity))

    # similarities est sous la forme d'une liste de tuple qui se présente sous cette forme par exemple :
    #      [(1, 0.002541010400780367), (2, 0.009072093485126885), (3, 0.01370473110839329), (4, 0.011269141152593542), (5, 0.00402094976692348), (6, 0.0016239725918885922), (7, 0.014392802677315311), (8, 0.007711421122439618)]

    maxi = 0
    nb_doc = 0

    # Récupération du nom du fichier avec la plus grande similarité
    for tuple in similarities:
        score = tuple[1]
        if score > maxi:
            maxi = score
            nb_doc = tuple[0]

    return nb_doc


# fonction intermédiaire qui en fonction du numéro du document envoie le nom du document
def nom_doc(nb_doc):
    """
    :param nb_doc: int
    :return: str
    """
    corpus = os.listdir('cleaned')
    return corpus[nb_doc-1]


"""
Cette fonction génère une réponse à partir d'une question donnée
"""
def generate_answer(question):
    """
    :param question: str
    :return: str
    """
    matrice = matrix_tf_idf_2('cleaned')

    nb_doc = pertinent_document(matrice, tf_idf_token(question), name_files('cleaned'))
    doc_sp = name_files('speeches')
    doc = doc_sp[nb_doc-1]

    # Extraire le mot avec le score TF-IDF le plus élevé du vecteur de la question
    #max_tfidf_word = max(question, key=lambda x: question[x])

    score_question = tf_idf_token(question)

    max_tfidf_word = None
    max_tfidf_score = -1  # Initialiser à une valeur négative, car les scores TF-IDF sont généralement positifs
    q_tf_idf = []
    l_question = question.split()
    cpt = 0
    # Parcourir le dictionnaire question pour trouver le mot avec le score TF-IDF le plus élevé
    for tfidf_score in score_question:
        if tfidf_score > max_tfidf_score:

            max_tfidf_score = tfidf_score

        if tfidf_score != 0:
            q_tf_idf.append(tfidf_score)
            max_tfidf_word = l_question[cpt]
            cpt += 1



    # Charger le document pertinent
    with open(os.path.join('./speeches', doc), 'r', encoding='utf-8') as file:
        content = file.read()

    """
    mot_impotant = high_tf_idf('cleaned')
    with open(os.path.join('./speeches', doc), 'r', encoding='utf-8') as f1:
        speech = f1.read()
        # Divise le texte en une liste de pharse
        content = speech.split(".")

        position_word = -1
        index = 0
        while index < len(content) and position_word == -1:

            # On trouve la position du mot dans la liste
            if mot_impotant in content[index]:
                position_word = index
            index += 1

        if position_word == -1:
            return None
        # On retourne la phrase entière de l'indice
        sentence = content[position_word]
        word_question = question.split()
        if word_question[0] in question_starters:
            final_sentence = question_starters[word_question[0]] + sentence
        else:
            final_sentence = sentence

    """
    # Trouver la première occurrence du mot dans le document et extraire la phrase qui le contient
    start_index = content.find(max_tfidf_word)
    end_index = content.find('.', start_index)

    rep = content[start_index:end_index + 1].strip()

    return  rep, max_tfidf_score, max_tfidf_word

    score = scalaire(a,b)/(norme_vecteur(a) * norme_vecteur(b))

"""
Cette fonction apporte plus de d'âme à la réponse générée
"""
def add_politeness(question, response):
    """
    :param question: str
    :param response: str
    :return: str
    """
    # Dictionnaire de débuts de questions et réponses associées
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"
    }

    # Extraire le début de la question
    question_words = question.split()
    question_starter = question_words[0] if question_words else None

    # Ajouter une réponse spécifique si le début de la question est connu
    if question_starter in question_starters:
        polite_response = question_starters[question_starter] + response
    else:
        polite_response = response

    return polite_response



