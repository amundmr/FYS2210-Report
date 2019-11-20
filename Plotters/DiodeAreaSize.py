import matplotlib.pyplot as plt
import numpy as np
import sys

#Reading file
f1 = open("../Data/w1Schottky/w1_iv_05mm","r")
f2 = open("../Data/w1Schottky/w1_iv_1mm","r")

Allfiles = [f1, f2]
Alldata = np.zeros((2,11))
i = 0
for file in Allfiles:
    file.readline()
    j=0
    for line in file.readlines():
        Alldata[i][j] = float(line.split()[1])
        j+=1
    i+=1

V = np.linspace(-1,1,11)
print(V)
print(Alldata)

#Plotting read data

plt.scatter(V,Alldata[0], label= "Area = 0.5mm")
plt.plot(V,Alldata[0])
plt.scatter(V,Alldata[1], label= "Area = 1mm")
plt.plot(V,Alldata[1])


plt.ylabel(r"Current, $I$ / [A]")
plt.xlabel(r"Voltage, $V$, / [V]")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title("I-V plot for differently sized diodes")
plt.yscale('log')
plt.legend()

plt.savefig("../Figures/DiodeAreaSize.png", bbox_inches='tight')
plt.show()
