import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import Eye
node = 'n77'
SampleName = 'sample'
Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node)