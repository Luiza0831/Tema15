import csv,json
# 3. Scrieti o functie care numara cate persoane sunt inregistrate in fisierul csv

calejson="Lista_Nume.json"
calecsv="Lista_json_to_csv.csv"
def numar_cate_linii_sunt_in_csv():
    count=0
    with open(calecsv,'r') as csvfile:
        reader = csv.reader(csvfile)
        # skip header
        next(reader)
        for line in reader:
            count+=1
    return count

print(f"In fisierul '{calecsv}' sunt {numar_cate_linii_sunt_in_csv()} persoane inregistrate.")

# 4. Scrieti o functie care identifica pe baza informatiilor din fisierul json generat la problema 1, persoana cea mai tanara din lista

def cea_mai_tanara_persoana_din_json():
    with open(calejson,'r') as jsonfile:
        lista=json.load(jsonfile)
        min=lista[0]["Varsta"]
        nume_prenume=f"{lista[0]["Nume"]} {lista[0]["Prenume"]}"
        for dict in lista:
            if dict["Varsta"]<min:
                min=dict["Varsta"]
                nume_prenume=f"{dict["Nume"]} {dict["Prenume"]}"
        return nume_prenume

print(f"Cea mai tanara persoana inregistrat in fisierul '{calejson}' este {cea_mai_tanara_persoana_din_json()}.")