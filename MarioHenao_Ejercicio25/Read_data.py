import numpy as np
import matplotlib.pylab as plt
import sys

def gauss(x,mu=3,sigma=1):
    return 1.0/np.sqrt(2*np.pi*sigma**2)*np.exp(-0.5*(x-mu)**2/sigma**2)
datos=sys.argv[1]
mu = float(sys.argv[2])
sigma = float(sys.argv[3])

archivo=np.genfromtxt("datos.txt")
a=archivo
x = np.linspace(-4*sigma+mu,4*sigma+mu)
plt.plot(x,gauss(x,mu,sigma))
plt.hist(a,bins=50,density=True)
plt.savefig("Histogram.pdf")
plt.close()
