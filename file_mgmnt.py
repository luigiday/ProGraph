import json

def write_csv(tableau, path):
    file = path.open("w")
    xy = tableau.get()
    for 