import csv,json
# 5. Scrieti o functie care va mari cu 1 varsta tuturor persoanelor din fisierul csv
calecsv="Lista_json_to_csv.csv"
def incrementez_varsta_din_csv():
    listacsv=[]
    with open(calecsv,'r') as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            header=line
            break
        listacsv.append(header)
        for line in reader:
            line[2]=int(line[2])+1
            listacsv.append(line)
    with open(calecsv,'w',newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(listacsv)

incrementez_varsta_din_csv()

# 6. Scrieti o functie care va mari cu 1 varsta tuturor persoanelor dinf fisierul json
calejson="Lista_Nume.json"
def incrementez_varsta_din_json():
    with open(calejson,'r') as jsonfile:
        listajson=json.load(jsonfile)
        for dict in listajson:
            dict["Varsta"]+=1
    with open(calejson,'w') as jsonfile:
        json.dump(listajson,jsonfile)

incrementez_varsta_din_json()