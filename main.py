# Scrieti o functie care citeste de la tastatura nume, prenume, varsta  de n ori (n citit de la tastatura) si salveaza informatiile intr-un fisier json.
import json, os, csv

def citeste_int(a):
    return int(input(a))

def import_lista_in_json(cale,lista):
    with open(cale,'w') as jsonfile:
        json.dump(lista,jsonfile)

calejson="Lista_Nume.json"

def citeste_n_ori():
    n=citeste_int("n=")
    if os.path.exists(calejson):
        with open(calejson,'r') as file:
            lista=json.load(file)
    else:
        lista=[]
    for i in range(n):
        dict={}
        dict["Nume"]=input("Nume: ")
        dict["Prenume"]=input("Prenume: ")
        dict["Varsta"]=citeste_int("Varsta: ")
        lista.append(dict)
    import_lista_in_json(calejson,lista)

citeste_n_ori()

# Scrieti o functie care citeste un fisier json de tipul celui de la problema 1 si scrie informatiile in format csv

calecsv="Lista_json_to_csv.csv"

def json_to_csv(calejson):
    with open(calejson,'r') as jsonfile:
        lista=json.load(jsonfile)
    header=["Nume","Prenume","Varsta"]
    listacsv=[]
    with open(calecsv,'w',newline='') as csvfile:
        listacsv.append(header)
        for dict in lista:
            listadict=[]
            for key in dict:
                listadict.append(dict[key])
            listacsv.append(listadict)
        writer=csv.writer(csvfile)
        writer.writerows(listacsv)

json_to_csv(calejson)