import json 

donnees = {
    
}
 # Les données sont sauvegardeer sous forme de dictionnaire 

with open("donnees.json", "w", encoding="utf-8") as fichier: # Enregistrement dans un fichier nommé "donnees.json"
    json.dump(donnees, fichier, ensure_ascii=False, indent=4) # Convertit le dictionnaire python au format json sur un fichier text lisible par l'homme.