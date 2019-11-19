import requests

url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
def lister_parties(idul):
    url = 'lister/'
    rep = requests.get(url_base+url, params={'idul': idul})
    return retourne_requests(rep, url)
def débuter_partie(idul):
    url = 'débuter/'
    rep = requests.post(url_base+url, data={'idul': idul})
    return retourne_requests(rep, url)
def jouer_coup(idul):
    url = 'jouer/'
    rep = requests.post(url_base+url, data={'idul': idul})
    return retourne_requests(rep, url)
def retourne_requests(rep, url):
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        return rep
    else:
        print(f"Le GET sur {url_base+url} a produit le code d'erreur {rep.status_code}.")