import argparse
import requests
import api

# à quoi va correspondre le x et le y
def annalyser_commande():
    allo = argparse.ArgumentParser()
    allo.add_argument(requests.get(x.api), help='position x')
    allo.add_argument(requests.get(y.api), help='position y')
    return allo.parseargs()
annalyser_commande()

#contraintes

def murs_horizontaux(x, y):
    if 1 <= x <= 8 and 2 <= y <= 9:
        return 'ok'
    else:
        return 'nok'

def afficher_damier_ascii():
    print('Légende: 1='+idul+', 2=automate')
    print('   -----------------------------------')
    #coordonnées en x

    #coordonnées en y



    print('--|----------------------------------- ')