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
def afficher_damier_ascii(dico):
    idul = (dictionnaire['état']['joueurs'][0]['nom'])
    print('Légende: 1='+idul+', 2=automate')
    print('   -----------------------------------')
    print('9 | . z . z . z . z . z . z . z . z . |')
    print('  | w v w v w v w v w v w v w z w v w |')
    print('8 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('7 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('6 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('5 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('4 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('3 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('2 | . z . z . z . z . z . z . z . z . |')
    print('  |   v   v   v   v   v   v   z   v   |')
    print('1 | . z . z . z . z . z . z . z . z . |')
    print('--|----------------------------------- ')
    print('  | 1   2   3   4   5   6   7   8   9 ')
    print(dictionnaire['état']['joueurs'][0])
#position du joueur
    print(dictionnaire['état']['joueurs'][0]['pos'])    
    #contraintes
#position des murs
#verticaux
    print(dictionnaire['murs']['verticaux'])
    #contraintes
#horizontaux
    print(dictionnaire['murs']['horizontaux'][0])
    #contraintes
analyser_commande()

#demander à l'utilisateur de spécifier son coup
#transmettre le coup au seveur
#repartir ligne 6