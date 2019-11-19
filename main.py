import argparse 
#contacter le serveur
import api

#faire une commande help
def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help='IDUL du joueur.')
    parser.add_argument('-l', '--lister', metavar='', help='Lister les identifiants de vos 20 dernères parties.')
    afficher_damier_ascii(api.débuter_partie(parser.parse_args().idul))
    return parser.parse_args()


#afficher un damier en art ascii
def afficher_damier_ascii():


#demander à l'utilisateur de spécifier son coup
#transmettre le coup au seveur
#repartir ligne 6