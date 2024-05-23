# Scrieti o functie care citeste de la tastatura nume, prenume, varsta  de n ori (n citit de la tastatura) si salveaza informatiile intr-un fisier json.
import json, os

def citeste_int(a):
    return int(input(a))

def import_lista_in_json(cale,lista):
    with open(cale,'w') as filejson:
        json.dump(lista,filejson)

cale="Lista_Nume.json"

def citeste_n_ori():
    n=citeste_int("n=")
    if os.path.exists(cale):
        with open(cale,'r') as file:
            lista=json.load(file)
    else:
        lista=[]
    for i in range(n):
        dict={}
        dict["Nume"]=input("Nume: ")
        dict["Prenume"]=input("Prenume: ")
        dict["Varsta"]=citeste_int("Varsta: ")
        lista.append(dict)
    import_lista_in_json(cale,lista)

citeste_n_ori()


