import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model
from sklearn.metrics import r2_score
from pathlib import Path
import os
abc = 'sample'
def RC(seg_length, voltage, node,SampleName):
    V = []
    capacitance = []
    resistance = []
    admittance = []
    file_p = os.path.abspath(__file__)
    file_p = file_p[:-15]
    file_p = os.path.join(file_p,'data',SampleName, node +'_CV_result_ac_des.plt' )
    f = open(file_p ,'r')
    lines = open(file_p,'r').readlines()   
    for i in range(len(lines)):
        if lines[i] == '      1.00000000000000E+09\n':
            split = lines[i + 1].split('   ')
            split = lines[i + 1]
            V.append(float(split[5:26]))
            capacitance.append(float(split[75:95]) * 1e15)  # [fF/um]
            admittance.append(-float(split[97:118]))  # [S/um]
            resistance.append((-float(split[97:118]) / ((2 * np.pi * 1e9) ** 2 * float(split[75:95]) ** 2)) / 1e3)
            # resistance.append(1/-float(split[]))

    fp1 = np.polyfit(V, resistance, 2)
    f1 = np.poly1d(fp1)
    Ad = f1(voltage)

    fp2 = np.polyfit(V, capacitance, 2)
    f2 = np.poly1d(fp2)
    Cp = f2(voltage)

    R = (f1(voltage) / ((2 * np.pi * 1e9) ** 2 * (f2(voltage) * 1e-15) ** 2)) / 1e3

    return fp1, fp2