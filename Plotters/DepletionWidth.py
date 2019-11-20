import matplotlib.pyplot as plt
import numpy as np
import sys

def func(V):
    e = 11.8*8.85e-14
    Vbi = 0.6
    qNd = 0.0001008
    W = np.sqrt((2*e*(Vbi-V))/(qNd))
    return W

V = np.linspace(0,-16, 17)
W = func(V)*1000


#Plotting read data


plt.scatter(V,W, label = "W", color = 'g')
plt.plot(V,W, linewidth=1)



plt.ylabel(r"Depletion Width, $W$, $[\mu m]$")
plt.xlabel(r"Reverse biased voltage, V / [V]")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title(r"Depletion zone width")
#plt.ylim(0,0.0006)
plt.legend()

plt.savefig("../Figures/DepletionWidth.png", bbox_inches='tight')
plt.show()
