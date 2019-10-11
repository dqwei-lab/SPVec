import pandas as pd
import numpy as np
import os

os.chdir('E:\\')
def read_data(filename):
    try:
        drug_target_data=pd.read_table(filename)
    except ImportError:
        print ('''Can't find the file!''')
drug_target_data=read_data('targets.txt')

def data_proprecessing(data):
    data = data['mol,BindingDB Target Chain Sequence'].tolist()
    feat = []

    for i in range(0,len(data)):
        feat.append(data[i].split(','))
    feat = pd.DataFrame(feat,columns=['mol','Target'])
    feat['Target']=feat['Target'].map(lambda x: x.replace(' ',''))
    feat['Target']=feat['Target'].map(lambda x: x.upper())
    feat['counts']=feat['mol'].map(lambda x: x.count('C'))
    feat = feat[feat.counts > 3 ].reset_index(drop = True)
    feat  = feat.drop('counts',axis=1)
    return feat

 def construct_dataset(data):   
    target=pd.DataFrame(data['Target'].unique())
    mol=pd.DataFrame(data['mol'].unique())
    tar= [ ]
    all_data = pd.DataFrame([ ])
    for i in range(len(target)):
        tar = pd.Series(list (target.iloc[i]) * len(mol))
        all = pd.concat([mol,tar],axis=1,ignore_index=True)
        all_data = pd.concat([all,all_data],axis=0,ignore_index=True)
    all_data = pd.DataFrame(all_data)
    all_data.columns=['mol','target']
    negtive_data = all_data.append(data)
    negtive_data.drop_duplicates(keep= False,inplace=True)
    negtive_data.reset_index(drop = True,inplace= True)
    negtive_data = shuffle(negtive_data)
    n = len(data)
    negtive_data_1 = negtive_data[0:n]
    negtive_data['Label']='0'
    data['Label']='1'
    data_1 = pd.concat([data,negtive_data_1],axis=0,ignore_index=True)
    return data_1