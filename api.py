import requests

urlBase = 'https://python.gel.ulaval.ca/quoridor/api/'
def lister_parties(idul):
    """Lister"""
    url = 'lister/'
    rep = requests.get(urlBase+url, params={'idul': idul})
    return retourne_requests(rep, url)
def débuter_partie(idul):
    """"Débuter"""
    url = 'débuter/'
    rep = requests.post(urlBase+url, data={'idul': idul})
    return retourne_requests(rep, url)
def jouer_coup(idul):
    """Jouer"""
    url = 'jouer/'
    rep = requests.post(urlBase+url, data={'idul': idul})
    return retourne_requests(rep, url)
def retourne_requests(rep, url):
    """Request"""
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        return rep

