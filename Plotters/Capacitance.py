import matplotlib.pyplot as plt
import numpy as np
import sys

#Reading file
#f = open(sys.argv[1],"r")
f = open("../Data/Schottky/w2_cv_1","r")
f.readline()
f.readline()
lines=f.readlines()
V = np.zeros(len(lines))
C = np.zeros_like(V)
cond = np.zeros_like(V)
depth = np.zeros_like(V)
doping = np.zeros_like(V)

i=0
for line in lines:
    V[i] = float(line.split()[0])
    C[i] = float(line.split()[1])
    cond[i] = float(line.split()[2])
    i += 1

C *= 1e12 #Making this shit in pF bro
#Plotting read data
plt.scatter(abs(V),C, label = "Capacitance", color = 'g')
plt.plot(abs(V),C, linewidth=1)
plt.ylabel(r"Capacitance, $C$, $[pF]$")
plt.xlabel(r"Voltage")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title(r"Capacitance over voltage")
#plt.yscale('log')
#plt.legend()

plt.savefig("../Figures/Capacitance.png", bbox_inches='tight')
plt.show()
