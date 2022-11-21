import sys, os, glob, set
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import Eye

# SampleName = 'sample'
# node = ''
node, SampleName = set.set_node_sam('','')
print(node, SampleName)
Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)