import csv
import numpy as np
import matplotlib.pyplot as plt
import hex2rgb as h2r

colors=[None]*2000
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
        if colors[coord[0]] is None:
            colors[coord[0]]=[None]*2000
        if colors[coord[0]][coord[1]] is None:
            colors[coord[0]][coord[1]]=dict()
        if color not in colors[coord[0]][coord[1]].keys():
            colors[coord[0]][coord[1]][color]=0
        colors[coord[0]][coord[1]][color]=colors[coord[0]][coord[1]][color]+1
    file.close()
for i in range(2000):
    print(i)
    for j in range(2000):
        pixel=(0,0,0)
        if colors[j][i] is not None:
            # pixel = h2r.hex_to_rgb(h2r.combine_hex_values(colors[j][i]))
            pixel = h2r.hex_to_rgb(max(colors[j][i], key=colors[j][i].get))
        final[i,j,0]=pixel[0]/255
        final[i,j,1]=pixel[1]/255
        final[i,j,2]=pixel[2]/255

plt.imshow(final,origin='upper')
plt.imsave('color_mode.png',final,origin='upper')
plt.show()