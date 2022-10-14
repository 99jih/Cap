from signal import signal
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot
from PySpice.Plot.BodeDiagram import bode_diagram

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

import PySpice
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
from src import RC_data as RC
from src import PRBS

# 회로 설계
def MZM(signal,seg_length,Zs, L0_init, C0_init,node): # RC 데이터 리스트 추가
    circuit = Circuit('Custom')

    source = circuit.PieceWiseLinearVoltageSource('input', 10, circuit.gnd, values=signal)
    
    [aRs, bRs, cRs] = RC.RC(500,0,node)[0]
    [aCj, bCj, cCj] = RC.RC(500,0,node)[1]
    
    circuit.R('z', 10, 1, Zs@u_Ω)
    circuit.C('0', 1, circuit.gnd, C0_init@u_F)
    circuit.R('s', 1, 2, 'R={ (%s*V(%s)**2 + %s*V(%s) + %s) *1000/%s*2}' % (aRs, 1, bRs, 1, cRs, seg_length))
    circuit.L('0', 2, 3, L0_init@u_H)
    circuit.C('j', 3, circuit.gnd, 'C={ (%s*V(%s)**2 + %s*V(%s) + %s) *%s*1e-15/2}' % (aCj, 3, bCj, 3, cCj, seg_length))    

    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    step_time = 2@u_ps
    analysis = simulator.transient(step_time=step_time, end_time=5000@u_ps)
    print('성공')
    return analysis


