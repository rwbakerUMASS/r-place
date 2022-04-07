import csv
import numpy as np
import matplotlib.pyplot as plt
import hex2rgb as h2r
import json

pctile=0.1 #top x percentile to remove
with open('top_contrib.json','r') as file:
    top_dict = json.load(file)
top_dict = dict(sorted(top_dict.items(), key=lambda item: item[1],reverse=True))
top_list = list(top_dict)
top_contribs = set(top_list[:int(len(top_dict)*pctile)])

final=np.zeros((2000,2000,3))
for i in range(78):
    filename = 'D:/r-place-data/2022_place_canvas_history-0000000000'+str(i).rjust(2,'0')+'.csv'
    print('Opening ',filename)
    file = open(filename)
    csvreader=csv.reader(file)
    next(csvreader)
    for row in csvreader:
        color=row[2][1:len(row[2])]
        coord = row[3]
        coord=list(map(int,coord.split(',')))
        x=coord[0]
        y=coord[1]
        id=row[1]
        if id not in top_contribs:
            pixel = h2r.hex_to_rgb(color)
            final[x,y,0]=pixel[0]/255
            final[x,y,1]=pixel[1]/255
            final[x,y,2]=pixel[2]/255     
    file.close()

plt.imshow(final,origin='upper')
plt.imsave('color_mode.png',final,origin='upper')
plt.show()