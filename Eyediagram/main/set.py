from src import Eye
import os,glob

def set_node_sam(node,SampleName):
    main_p = os.path.abspath(__file__) 
    main_p = main_p[:-7]

    # sample list 만들기
    sam_p = os.path.join(main_p,'data','*')
    sample_list = glob.glob(sam_p)
    for i in range(len(sample_list)):
        sample_list[i] = sample_list[i].replace(sam_p[:-1],'')

    for j in range(len(sample_list)):
        SampleName = sample_list[j]
        
        # data/SampleName 에서 파일 받아와서 노드  리스트 만들기
        node_p = os.path.join(main_p,"data",SampleName)
        node_list = []
        node_list = [file for file in os.listdir(node_p) if file.endswith('_굴절률.txt')]
        for i in range(len(node_list)):
            node_list[i] = node_list[i].replace('_굴절률.txt','')
        node_list = sorted(node_list)
        
        # node input
        print_node = ', '.join(node_list)
        node_in = input(SampleName +' 폴더의 [' + print_node + '] 중 결과 원하는 노드 입력(전체:all)(여러개일 경우 사이에 공백):')
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
                print(node)     #지우기
                node = nodes[i]
                Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)