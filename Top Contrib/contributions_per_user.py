import json
import matplotlib.pylab as plt

with open('top_contrib.json','r') as file:
    contrib=json.load(file)
contrib = dict(sorted(contrib.items(), key=lambda item: item[1],reverse=True)).values()

plt.plot(contrib)
plt.show()
