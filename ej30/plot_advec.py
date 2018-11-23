import numpy as np
import matplotlib.pylab as plt

archivo = np.genfromtxt("./serial_files_advec/Estado_inicial.txt") #serial plot
X = archivo[:,0]
U = archivo[:,1]
plt.plot(X,U,alpha=0.5,label='serial ini')
archivo = np.genfromtxt("./serial_files_advec/Estado_10.txt")
X = archivo[:,0]
U = archivo[:,1]
plt.plot(X,U,alpha=0.5,label='serial fin')

archivo = np.genfromtxt("./parallel_files_advec/Estado_inicial.txt") #parallel plot
X = archivo[:,0]
U = archivo[:,1]
plt.plot(X,U,'--',label='parallel ini')
archivo = np.genfromtxt("./parallel_files_advec/Estado_10.txt")
X = archivo[:,0]
U = archivo[:,1]
plt.plot(X,U,'--',label='parallel fin')

plt.legend()
plt.savefig('advec_comparison.pdf')
plt.close()