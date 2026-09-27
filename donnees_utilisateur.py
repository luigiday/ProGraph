import json 

donnees = {
    "prénom" : "noah"
}
 # Les données sont sauvegardeer sous forme de dictionnaire 

with open("donnees.json", "w", encoding="utf-8") as fichier: # Enregistrement dans un fichier nommé "donnees.json"
    json.dump(donnees, fichier, ensure_ascii=False, indent=4) # Convertit le dictionnaire python au format json sur un fichier text lisible par l'homme.

with open("donnees.json", "r", encoding="utf-8") as fichier: 
    donnees = json.load(fichier) # Charge le fichier json en dictionnaire python.
    print(donnees) # Affiche le dictionnaire python des données chargées.