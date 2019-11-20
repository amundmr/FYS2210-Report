import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy import stats

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

#C *= 1e12 #Making this shit in pF bro
OneOverCSquared = 1/(C**2)

slope, intercept, r_value, p_value, std_err = stats.linregress(abs(V), OneOverCSquared)
print("slope: %f    intercept: %f" % (slope, intercept))


#Plotting read data
plt.axhline(y=0, color = "black", linestyle = "--")
plt.plot(range(-1,19), intercept + slope*range(-1,19), color = 'r', label='Fitted line, slope = %g'%slope, linestyle = "--")
plt.scatter(abs(V),OneOverCSquared, label = "Inverse squared capacitance", color = 'g')
plt.plot(abs(V),OneOverCSquared, linewidth=1)
plt.scatter(-0.6, 0, color = "r", label = r"intersection in $V = -0.6$V")


plt.ylabel(r"Inverse capacitance squared, $\frac{1}{C^2}$, $[\frac{1}{(F)^2}]$")
plt.xlabel(r"Reverse biased voltage, V / [V]")
plt.tick_params(direction='in', top = 'true', right = 'true')
plt.title(r"Inverse capacitance squared over voltage")

#plt.xlim(-1, 17)
#plt.ylim(-0.001,0.006)
#plt.yscale('log')
plt.legend()

plt.savefig("../Figures/InvSqrCapacitance.png", bbox_inches='tight')
plt.show()
