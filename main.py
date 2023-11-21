# Programme principal du projet

from functions import *


def main():  # Fonction principale, execute le programme entier
    return


if __name__ == "__main__":
    names = name_files("speeches")
    #print_names(names)
    # main() - on execute la fonction principale

    print(lowercase('speeches/Nomination_Chirac1.txt', 'cleaned/clean_text.txt'))
    #print(punctuation('speeches/Nomination_Chirac1.txt'))
    print(punctuation('cleaned/clean_text.txt', 'cleaned/clean_text2.txt'))
    print(tf('cleaned/clean_text2.txt'))