#Programme principal du projet

from functions import *

if __name__ == "__main__":
    names = nom_fichiers("speeches")
    print_names(names)