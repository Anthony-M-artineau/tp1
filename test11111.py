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

def afficher_damier_ascii(dictionnaire):
print('Légende: 1=idul, 2=automate')
print('   -----------------------------------')
print('9 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('8 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('7 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('6 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('5 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('4 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('3 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('2 | .   .   .   .   .   .   .   .   . |')
print('  |                                   |')
print('1 | .   .   .   .   .   .   .   .   . |')
print('--|-----------------------------------')
print('  | 1   2   3   4   5   6   7   8   9')