import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src import Eye

SampleName = 'sample'
# node = ''
node_in = input('결과 원하는 노드 입력(전체:all)(여러개일 경우 사이에 공백):')

# data/sample 에서 파일 받아와서 노드  리스트 만들기
node_p = os.path.abspath(__file__)
node_p = node_p.replace("run.py",("data/"+SampleName))
node_list = [file for file in os.listdir(node_p) if file.endswith('_굴절률.txt')]
for i in range(len(node_list)):
    node_list[i] = node_list[i].replace('_굴절률.txt','')

# input 받은 값으로 실행
if node_in == 'all':
    for i in range(len(node_list)):
        node = node_list[i]
        Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
elif node_in in node_list:
    node = node_in
    Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)
else:
    nodes = node_in.split(' ')
    for i in range(len(nodes)):
        node = nodes[i]
        Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)
