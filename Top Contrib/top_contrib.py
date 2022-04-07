import csv
import json

contrib = dict()

for i in range(78):
    filename = 'D:/r-place-data/2022_place_canvas_history-0000000000'+str(i).rjust(2,'0')+'.csv'
    print('Opening ',filename)
    file = open(filename)
    csvreader=csv.reader(file)
    next(csvreader)
    for row in csvreader:
        id=row[1]
        if id not in contrib.keys():
            contrib[id]=0
        contrib[id]=contrib[id]+1
    file.close()

contrib = dict(sorted(contrib.items(), key=lambda item: item[1],reverse=True))
with open('top_contrib.json','w') as file:
    json.dump(contrib,file)