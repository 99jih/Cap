import os
def pmax(seg_length,node):
    path = str(os.getcwd()).replace("src", "")
    f = open(f'{path}' + '/data/sample/' + node + '_phase-shifter loss.txt', 'r')

    line = f.readline()
    loss = line.split(',')
    loss.pop()
    loss = list(map(float,loss))
    
    PS_length = seg_length*1e-6 #seg_length [um]
    Pin = 0 #dBm
    # IL = (loss[0]+loss[-1])/2*PS_length*1e2 #Inserption loss 
    IL = loss[1]*PS_length*1e2 # 0V 일때의 loss -> Pmax
    pmax = 10**((Pin-IL)/10)
    # pmax = 10**((IL)/10)
    return float(pmax)