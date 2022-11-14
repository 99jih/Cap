import numpy as np
import matplotlib.pyplot as plt
import sympy
from fractions import Fraction
import os

def neff_voltage(wl,node,SampleName):
    voltage = [0,-0.5,-1,-1.5,-2]
    file_p = os.path.abspath(__file__)
    file_p = file_p.replace('src/neff.py',('data/'+SampleName+'/'))
    f = open(file_p + node+"_굴절률.txt",'r')

    line = f.readline()
    neff = line.split(',')
    neff.pop()
    neff = list(map(float,neff))
    f.close()

    # plt.plot(voltage,neff)
    # plt.show()

    ppp = []
    iintensity = []
    for i in range(len(neff)):
        pppp = 2*np.pi*neff[i]/wl*500
        ppp.append(pppp)
    ppp.pop(0)

    phases = []
    intensity = []

    fp1 = np.polyfit(voltage,ppp,2)
    f1 = np.poly1d(fp1)

    intensity = np.cos(np.pi/4 + f1(voltage)/2)**2

    x = sympy.symbols('x')
    f = sympy.Eq(f1(x),float(ppp[-1]/2))
    result_voltage = sympy.solve(f)
    result1 = np.cos(f1(float(result_voltage[-1])))**2

    
    return float(result_voltage[-1])