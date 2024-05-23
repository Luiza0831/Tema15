import csv
# Scrieti o functie care numara cate persoane sunt inregistrate in fisierul csv

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