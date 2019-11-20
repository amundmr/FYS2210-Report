import matplotlib.pyplot as plt
import numpy as np
import sys

#Reading file
f1 = open("../Data/Schottky/w2_iv_05_ideality","r")



Alldata = np.zeros(101)

f1.readline()
j=0
for line in f1.readlines():
    Alldata[j] = float(line.split()[1])
    j+=1

V = np.linspace(0,1,101)
print(V)
print(Alldata)

#Plotting read data
V = V[:50]
A = np.log(Alldata[:50])

plt.scatter(V,A, label = "IV curve", s = 20)
plt.plot(V,A, linewidth=1)


#Burde brukt scipy linregress
slope = 37

plt.plot(V,slope*V-18.7, label = "Slope = %.1f"%slope, linestyle = "--", color = "r")


plt.ylabel(r"Current, $I$ / [$ln(A)$]")
plt.xlabel(r"Voltage, $V$ / [V]")

plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title("Current over voltage, V. natural log Y-scale")
plt.xlim(0,0.5)

plt.ylim(-20, -7)
#plt.yscale('log')
plt.legend()

plt.savefig("../Figures/DiodeZoom.png", bbox_inches='tight')
plt.show()
