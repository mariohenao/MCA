import numpy as np
import matplotlib.pylab as plt

archivo = np.genfromtxt("./serial_files_walk/walk.txt") #serial plot
plt.hist(archivo,bins=100,alpha=0.5,normed=True,label='serial',color='blue')

archivo = np.genfromtxt("./parallel_files_walk/walk.txt") #parallel plot
plt.hist(archivo,bins=100,alpha=0.5,normed=True,label='parallel',color='teal')

plt.legend()
plt.savefig('histogram_comparison_walk.pdf')
plt.close()
