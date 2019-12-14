"""
    A python script allowing Students at UPS to connect easily to the campus WIFI.
"""

import requests

LOGIN = "LOGIN"
PASSWORD = "Pass"


def try_access_point(i):
    url = f'https://pfrf0${i}.in.crous-toulouse.fr:8003/index.php?zone=lan'
    try:
        requests.post(url)
        return url
    except:
        return None


def try_all_access_point():
    i = 0
    url = None
    while i <= 5 and url is None:
        url = try_access_point(i)
        i += 1
    return url


def connect(url):
    print(f'Url used : {url}')

    data = {
        "auth_user": LOGIN, "auth_pass": PASSWORD,
        "redirurl": "http://www.crous-toulouse.fr/",
        "accept": "Continue"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": url
    }

    res = requests.post(url, data=data, headers=headers)

    if res.content == b'You are connected.':
        input("Déjà Connecté")
    elif b'Erreur d\'Authentification !' in res.content[:224]:
        input("Mauvais Identifiants")
    elif b'Redir' in res.content[:50]:
        input("Connecté !")


if __name__ == '__main__':
    url = try_all_access_point()
    if url is None:
        input("Impossible de se connecter !")
        exit(1)
    else:
        connect(url)
