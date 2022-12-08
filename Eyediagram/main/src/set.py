from src import Eye, test
import os,glob

def set_node_sam(node,SampleName):
    main_p = os.path.abspath(__file__)
    main_p = main_p[:-11]

    # sample list 만들기
    sam_p = os.path.join(main_p,'data')
    sample_list = os.listdir(sam_p)
    print_sam = ', '.join(sample_list)

    fold_in = input('['+print_sam+'] 중 결과 원하는 폴더 입력(전체:all)(여러개일 경우 사이에 공백):')
    if fold_in == 'all':
        samples = sample_list
    else:
        samples = fold_in.split(' ') 
    
    node_in = input('결과 원하는 노드 입력(전체:all)(여러개일 경우 사이에 공백): ')
    if node_in == 'all':
        for i in range(len(samples)):
            SampleName = samples[i]
            test.test(SampleName)
            
            node_p = os.path.join(main_p,"data",SampleName)
            node_list = []
            node_list = [file[:-8] for file in os.listdir(node_p) if file.endswith('_굴절률.txt')] 
            node_list = sorted(node_list)
            
            for j in range(len(node_list)):
                node = node_list[j]
                Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
    else:
        nodes = node_in.split(' ')
        
        for i in range(len(samples)):
            SampleName = samples[i]
            test.test(SampleName)
            for j in range(len(nodes)):
                node = nodes[j]
                try:
                    Eye.Eye(50,2,-2,0,500,25,0.176e-9,26e-15,1.31,node,SampleName) 
                except:
                    print(SampleName, '폴더 내에',node,'가 없습니다.')
                    continue