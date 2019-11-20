import matplotlib.pyplot as plt
import numpy as np
import sys

#Reading file
f1 = open("../Data/Schottky/w2_iv_05","r")
f2 = open("../Data/Schottky/w2_iv_05_lys","r")

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

plt.scatter(V,Alldata[0], label= "Closed box", color = "black")
plt.plot(V,Alldata[0], color = "black")

plt.scatter(V,Alldata[1], label= "Roomlight", color = "#b58800")
plt.plot(V,Alldata[1], color = "#b58800")


plt.ylabel(r"Current, $I$ / [A]")
plt.xlabel(r"Voltage, $V$, / [V]")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title("Current over voltage, V")
plt.yscale('log')
plt.legend()

plt.savefig("../Figures/DiodeCharacteristics.png", bbox_inches='tight')
plt.show()
