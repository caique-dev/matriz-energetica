import csv
with open('/home/caique/repos/matriz-energetica/data/paises_com_continente_subcontinente_area.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i=0
    for row in spamreader:
        i+=1

    print(i)