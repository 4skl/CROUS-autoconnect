import requests
login = "Login"
password = "Pass"
goodUrl = str()
for i in range(1,5):
    url = "https://pfrf0"+str(i)+".in.crous-toulouse.fr:8003/index.php?zone=lan"
    try:
        requests.post(url)
        goodUrl = url
        break
    except:
        pass
if goodUrl == '':
    for i in range(1,5):
        url = "https://wifi-gw"+str(i)+"-ups.private.univ-tlse3.fr:8003/index.php?zone=ssid_ups"
        try:
            requests.post(url)
            goodUrl = url
            break
        except:
            pass
if goodUrl == '':
    input("Non Connecté (vous n'êtes pas connecté a un point d'accès du CROUS, ou celui-ci n'est pas encore référencé)")
    exit()
print("Url used : ", goodUrl)
data = {"auth_user": login, "auth_pass": password, "redirurl": "http://www.crous-toulouse.fr/","accept": "Continue" }
headers = {"Content-Type": "application/x-www-form-urlencoded", "Origin" : goodUrl}
res = requests.post(goodUrl, data=data, headers=headers)
if res.content == b'You are connected.':
    input("Déjà Connecté")
elif b'Erreur d\'Authentification !' in res.content[:224]:
    input("Mauvais Identifiants")
elif b'Redir' in res.content[:50]:
    input("Connecté !")
