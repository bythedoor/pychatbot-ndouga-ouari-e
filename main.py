# Programme principal du projet

from functions import *


def main():  # Fonction principale, execute le programme entier
    return


if __name__ == "__main__":
    names = name_files("speeches")
    print_names(names)
    # main() - on execute la fonction principale
    #print(occurence("la", 'speeches/Nomination_Chirac1.txt'))
    #print(lowercase('speeches/Nomination_Chirac1.txt', 'clean_text.txt'))
    print(punctuation('speeches/Nomination_Chirac1.txt', 'clean_text.txt'))