from time import time
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import os

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
from src import PRBS, circuit, pmax
from src import neff as n

def Eye(datarate, delay, V_low, V_high, seg_length, Zs, Rm_init, Cm_init ,wl,node,SampleName): #wl[um]
    pico = 1e-12
    period = 1/datarate * 1e3 #ps
    pattern = period *4 * pico
    signal = PRBS.PRBS(datarate, 2, -2, 0) # 시그널 생성
    # signal = PRBS.PRBS_PAM4(datarate, -2, -1.1,-0.6, 0, 2)
    # signal = PRBS.PRBS_PAM4(datarate, -2, -1.15, -0.65, 0, 2)
    analysis = circuit.MZM(signal, seg_length, Zs, Rm_init, Cm_init,node,SampleName) # 회로 설계


    # index = circuit.MZM(signal, seg_length, Zs, Rm_init, Cm_init)[1]
    # node = str(10*index+4)

    num = int(np.array(analysis.time)[-1]/pattern)
    for k in range(num):
        globals()[f'time_{k}'] = []
        globals()[f'voltage_{k}'] = []
        for i in range(len(np.array(analysis.time))):
            if pattern*k <= float(np.array(analysis.time)[i]) < pattern*(k+1):
                globals()[f'time_{k}'].append((float(np.array(analysis.time)[i])-float(pattern*k))*1e12)
                globals()[f'voltage_{k}'].append(float(np.array(analysis['3'])[i]))

    # wl = 1.31 #um
    voltage = [0.5,0,-0.5,-1,-1.5,-2]
    file_p = os.path.abspath(__file__)
    file_p = file_p[:-11]
    file_p = os.path.join(file_p,'data',SampleName, node +'_굴절률.txt' )
    f = open(file_p ,'r')
    line = f.readline()
    neff = line.split(',')
    neff.pop()
    neff = list(map(float,neff))
    f.close()

    fp1 = np.polyfit(voltage,neff,2)
    f1 = np.poly1d(fp1)
    
    ori = n.neff_voltage(wl,node,SampleName)

    for k in range(num):
        globals()[f'intensity_{k}'] = []
        for i in range(len(globals()[f'voltage_{k}'])):
            neff1 = f1(globals()[f'voltage_{k}'][i])
            phase = 2*np.pi*neff1*500/wl - 2*np.pi*f1(ori)*500/wl
            Intensity = pmax.pmax(seg_length,node,SampleName)*np.cos(np.pi/4 + phase)**2 #phase 계산 방식 변경
            globals()[f'intensity_{k}'].append(Intensity)

    def create_folder(directory):
        os.makedirs(f'{directory}\\{SampleName}')

    fold_p = os.path.abspath(__file__)

    # file_p = file_p[:-11]
    # file_p = os.path.join(file_p,'data',SampleName, node +'_굴절률.txt' )
    # f = open(file_p ,'r')
    fold_p = fold_p[:-11]
    fold_p = os.path.join(fold_p,'res',SampleName)
    os.makedirs(fold_p,exist_ok=True)

    plt.figure(figsize=(9,8))        
    for k in range(num):
        plt.plot(globals()[f'time_{k}'],globals()[f'intensity_{k}'],'b', linestyle = 'solid', linewidth = 2)
    plt.ylabel('Optical output power [mW]',fontsize = '35')
    plt.xlabel('Time [ps]',fontsize = '35')
    plt.xticks(fontsize = '30')
    plt.yticks(fontsize = '30')
    plt.ylim(0,1)
    # plt.savefig(f"{fold_p}\\{node}_{str(Zs)}.png",bbox_inches = 'tight')
    os.chdir(fold_p)
    plt.savefig(f"{node}_{str(Zs)}.png",bbox_inches = 'tight')