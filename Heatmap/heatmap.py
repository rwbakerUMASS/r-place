import csv
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

freq=numpy.zeros((2000,2000))
for i in range(78):
    print(i)
    file = open('D:/r-place-data/2022_place_canvas_history-0000000000'+str(i).rjust(2,'0')+'.csv')
    csvreader=csv.reader(file)
    next(csvreader)
    for row in csvreader:
        coord = row[3]
        coord=list(map(int,coord.split(',')))
        freq[coord[0],coord[1]]=freq[coord[0],coord[1]]+1
    file.close()
nonzero_mean = freq.sum()/numpy.count_nonzero(freq)
std = freq.std()
cutoff = nonzero_mean+(3*std)
freq[freq>cutoff]=cutoff
ax=sns.heatmap(numpy.transpose(freq))
plt.show()