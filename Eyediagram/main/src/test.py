import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os, glob

def test(SampleName):
    SampleName = SampleName
    csv_list = []
    # filename = 'SiGe_density_Copy.csv'
    sam_p = os.path.join(os.path.abspath(__file__)[:-12],'data',SampleName,'*.csv') 
    csv_list = glob.glob(sam_p)

    for i in range(len(csv_list)):
        filename = csv_list[i]
        df = pd.read_csv(filename)

        loss = df.loc[:,'loss at 0V (dB/cm)'].tolist()
        VpiL = df.loc[:,'VpiL at 2Vpp(Vcm)'].tolist()
        capacitance_0V = df.loc[:,'C_0V[fF/um]'].tolist()
        capacitance_1V = df.loc[:,'C_-1V[fF/um]'].tolist()
        capacitance_2V = df.loc[:,'C_-2V[fF/um]'].tolist()
        resistance_0V= df.loc[:,'R_0V[ohm*mm]'].tolist()
        resistance_1V = df.loc[:,'R_-1V[ohm*mm]'].tolist()
        resistance_2V = df.loc[:,'R_-2V[ohm*mm]'].tolist()
        fcutoff_0V = df.loc[:,'f_0V[GHz]'].tolist()
        fcutoff_1V = df.loc[:,'f_-1V[GHz]'].tolist()
        fcutoff_2V = df.loc[:,'f_-2V[GHz]'].tolist()
        OMA_0V_dBm = df.loc[:,'OMA_500_0V [dBm]'].tolist()
        OMA_1V_dBm = df.loc[:,'OMA_500_-1V[dBm]'].tolist()
        OMA_2V_dBm = df.loc[:,'OMA_500_-2V[dBm]'].tolist()


        # Vol = ['0V', '1V', '2V']
        # for i in range(2):
        #     for v in Vol:
        #         globals()[f'OMA_{v}_dBm'].pop(0)
        #         globals()[f'fcutoff_{v}'].pop(0)
        #         globals()[f'capacitance_{v}'].pop(0)
        #         globals()[f'resistance_{v}'].pop(0)
        #     loss.pop(0)
        #     VpiL.pop(0)
        
        xvalue = [(6+ 2*i) for i in range(len(loss))]       
        xlabel = r'SiGe hDensity [10$^{17}$ cm$^{-3}]$'
        
        #fig 저장위치
        fig_p = os.path.join(os.path.join(os.path.abspath(__file__)[:-12],'res',SampleName))
        os.makedirs(fig_p,exist_ok=True)
        os.chdir(fig_p)
        
        #저항 결과
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, resistance_0V, 'ro-', linewidth = 3, markersize = 10, label = '0V')
        plt.plot(xvalue, resistance_1V, 'go-', linewidth = 3, markersize = 10, label = '-1V')
        plt.plot(xvalue, resistance_2V, 'bo-', linewidth = 3, markersize = 10, label = '-2V')
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel('R [Ohm*mm]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best', fontsize = '30', frameon = False)
        plt.savefig('Resistance.png',bbox_inches = 'tight')
        plt.clf()
        
        #OMA 결과
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, OMA_0V_dBm, 'ro-', linewidth = 3, markersize = 10, label = '0V')
        plt.plot(xvalue, OMA_1V_dBm, 'go-', linewidth = 3, markersize = 10, label = '-1V')
        plt.plot(xvalue, OMA_2V_dBm, 'bo-', linewidth = 3, markersize = 10, label = '-2V')
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel('OMA [dBm]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best', fontsize = '25', frameon = False)
        plt.savefig('OMA.png',bbox_inches = 'tight')
        plt.clf()

        #Cap 결과
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, capacitance_0V, 'ro-', linewidth = 3, markersize = 10, label = '0V')
        plt.plot(xvalue, capacitance_1V, 'go-', linewidth = 3, markersize = 10, label = '-1V')
        plt.plot(xvalue, capacitance_2V, 'bo-', linewidth = 3, markersize = 10, label = '-2V')
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel('C [fF/um]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best',fontsize = '25', frameon = False)
        plt.savefig('Cap.png',bbox_inches = 'tight')
        plt.clf()

        #frequency 결과
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, fcutoff_0V, 'ro-', linewidth = 3, markersize = 10, label = '0V')
        plt.plot(xvalue, fcutoff_1V, 'go-', linewidth = 3, markersize = 10, label = '-1V')
        plt.plot(xvalue, fcutoff_2V, 'bo-', linewidth = 3, markersize = 10, label = '-2V')
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel(r'$f_{cutoff}$ [GHz]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best', fontsize = '25', frameon = False)
        plt.savefig('Frequency.png',bbox_inches = 'tight')
        plt.clf()

        #VpiL
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, VpiL, 'ko-', linewidth = 3, markersize = 10)
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel(r'$V_\pi$L at 2$V_{pp}$ [Vcm]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best', fontsize = '30', frameon = False)
        plt.savefig('VpiL.png',bbox_inches = 'tight')
        plt.clf()

        #loss
        # plt.figure(figsize = (6,6))
        plt.plot(xvalue, loss, 'ko-', linewidth = 3, markersize = 10)
        plt.xlabel(xlabel,fontsize = '25')
        plt.ylabel('PS-loss at 0V [dB/cm]',fontsize = '25')
        plt.xticks(fontsize = '25')
        plt.yticks(fontsize = '25')
        plt.legend(loc = 'best',fontsize = '25', frameon = False)
        plt.savefig('loss.png',bbox_inches = 'tight')
        plt.clf()

