import argparse 


#faire une commande help
def analyser_commande():
    """Commande"""
    parser = argparse.ArgumentParser(
        description='Jeu Quoridor - phase 1'
        )
    parser.add_argument(
        'idul', help='IDUL du joueur.'
        )
    parser.add_argument(
        '-l', '--lister', metavar='', help='Lister les identifiants de vos 20 dernères parties.'
        )
    return parser.parse_args()
