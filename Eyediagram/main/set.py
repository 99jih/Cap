from src import Eye
import os,glob

def set_node_sam(node,SampleName):
    main_p = os.path.abspath(__file__)
    main_p = main_p[:-7]

    # sample list 만들기
    sam_p = os.path.join(main_p,'data')
    sample_list = os.listdir(sam_p)
    print_sam = ', '.join(sample_list)

    # 11/28수정
    node_in = input('결과 원하는 노드 입력(전체:all)(여러개일 경우 사이에 공백): ')
    if node_in == 'all':
        sample_in = input(print_sam + ' 중 원하는 폴더명 입력(전체 : all): ')
        
        if sample_in == 'all':
            for i in range(len(sample_list)):
                SampleName = sample_list[i]
                node_p = os.path.join(main_p,"data",SampleName)
                node_list = []
                node_list = [file[:-8] for file in os.listdir(node_p) if file.endswith('_굴절률.txt')]
                
                for j in range(len(node_list)):
                    node = node_list[i]
                    Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
        
        else: #all 일 경우 samples에 모두 추가하고 한번에 실행되도록 바꿀 수 있음(바꾸기)
            samples = sample_in.split(' ') 
            for i in range(len(samples)):
                SampleName = samples[i]
                
                node_p = os.path.join(main_p,"data",SampleName)
                node_list = []
                node_list = [file[:-8] for file in os.listdir(node_p) if file.endswith('_굴절률.txt')] 
                
                for j in range(len(node_list)):
                    node = node_list[i]
                    Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
    else:
        nodes = node_in.split(' ')
        for i in range(len(sample_list)):
            SampleName = sample_list[i]
            node_p = os.path.join(main_p,"data",SampleName)
            node_list = []
            node_list = [file[:-8] for file in os.listdir(node_p) if file.endswith('_굴절률.txt')] 
            
            for j in range(len(nodes)):
                node = nodes[i]
                Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 




    # for j in range(len(sample_list)):
    #     SampleName = sample_list[j]
        
    #     # data/SampleName 에서 파일 받아와서 노드  리스트 만들기
    #     node_p = os.path.join(main_p,"data",SampleName)
    #     node_list = []
    #     node_list = [file for file in os.listdir(node_p) if file.endswith('_굴절률.txt')]
        
    #     for i in range(len(node_list)):
    #         node_list[i] = node_list[i].replace('_굴절률.txt','')
    #     node_list = sorted(node_list)
        
    #     # node input
    #     print_node = ', '.join(node_list)
    #     node_in = input(SampleName +' 폴더의 [' + print_node + '] 중 결과 원하는 노드 입력(전체:all)(여러개일 경우 사이에 공백):')
    #     # input 받은 값으로 실행
    #     if node_in == 'all':
    #         for i in range(len(node_list)):
    #             node = node_list[i]
    #             Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
    #     elif node_in in node_list:
    #         node = node_in
    #         Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)
    #     else:
    #         nodes = node_in.split(' ')
    #         for i in range(len(nodes)):
    #             node = nodes[i]
    #             Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName)