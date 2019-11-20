import matplotlib.pyplot as plt
import numpy as np
import sys

#Reading file
#f = open(sys.argv[1],"r")
f1 = open("../Data/10um/w2_vg_1v_10um_50x50","r")
f2 = open("../Data/10um/w2_vg_2v_10um_50x50","r")
f3 = open("../Data/10um/w2_vg_3v_10um_50x50","r")
f4 = open("../Data/10um/w2_vg_4v_10um_50x50","r")
f5 = open("../Data/10um/w2_vg_5v_10um_50x50","r")

Allfiles = [f1, f2, f3, f4, f5]
Alldata = np.zeros((5,21))
i = 0
for file in Allfiles:
    file.readline()
    j=0
    for line in file.readlines():
        Alldata[i][j] = float(line.split()[2])
        j+=1
    i+=1

Vd = np.linspace(0,8,21)
#print(Vd)
#print(Alldata)

#Plotting read data
for i in range(len(Alldata)):
    plt.scatter(Vd,Alldata[i]*1000,s = 20, label= r"$V_G =$ %d $V$"%float(i+1))
    plt.plot(Vd,Alldata[i]*1000, linewidth=1)

plt.ylabel(r"Drain current, $I_d$ / [mA]")
plt.xlabel(r"Drain voltage, $V_d$, / [V]")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title(r"Current with different gate voltages, $10um$, $50x50$")
#plt.yscale('log')
plt.ylim(0,13.5)
plt.legend(loc="upper left")

plt.savefig("../Figures/I-V_10um_50x50.png", bbox_inches='tight')
#plt.show()
