import json

donnees = {}

# Conversion en chaîne JSON
donnees_json = json.dumps(donnees, indent=4)

# Affichage de la chaîne JSON
print(donnees_json)

# Enregistrement des données JSON dans un fichier
with open('donnees_utilisateur.json', 'w') as fichier:
    json.dump(donnees, fichier, indent=4)