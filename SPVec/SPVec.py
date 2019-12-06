
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import gensim 
import jieba
from gensim.models import Word2Vec 
import random 
import re
import os 



class SPVec:

    def __init__(self,filename):
        self.filename = filename
   
    def read_data(self):
        data=pd.read_csv(self.filename)
        return data

    def SMILES2Vec(self,dims,window_size,negative_size):
        SMILES_vec = pd.DataFrame()
        dictionary=[]
        Index = []
        data=self.read_data()
        texts = [[word for word in re.findall(r'.{3}',document)] for document in list(data)]
        model = Word2Vec(texts,size=dims,window=window_size,min_count=1,negative=negative_size,sg=1,sample=0.001,hs=1,workers=4)
        vectors = pd.DataFrame([model[word] for word in (model.wv.vocab)])
        vectors['Word'] = list(model.wv.vocab)

        for i in range(len(data)):
            Index.append(i)
        # 'Word' segmentation
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(Index[i])    
            dictionary.extend(i_word)
        SMILES_vec['Id'] = dictionary
        
        # substructure vectors generation
        dictionary=[]
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(texts[i][w])    
            dictionary.extend(i_word)
        SMILES_vec['Word'] = dictionary
        del dictionary,i_word
        
        SMILES_vec = SMILES_vec.merge(vectors,on='Word', how='left')
        SMILES_vec.columns = ['Id']+['word']+["vec_{0}".format(i) for i in range(0,dims)]
        SMILES_vec=SMILES_vec.drop('Word',axis=1)
   
        #Molecular Structure  Representation

        name = ["vec_{0}".format(i) for i in range(0,dims)]
        drug_embeddings = pd.DataFrame(SMILES_vec.groupby(['Id'])[name].agg('mean')).reset_index()
        drug_embeddings.columns=["Index"]+["mean_ci_{0}".format(i) for i in range(0,dims)]
        drug_embeddings.to_csv('drug_embeddings.csv',index=False)
        
        return SMILES_vec,drug_embeddings

    
    def ProtVec(self,dims,window_size,negative_size):
        Prot_vec = pd.DataFrame()
        dictionary=[]
        Index = []
        data=self.read_data()
        texts = [[word for word in re.findall(r'.{3}',document)] for document in list(data)]
        model = Word2Vec(texts,size=dims,window=window_size,min_count=1,negative=negative_size,sg=1,sample=0.001,hs=1,workers=4)
        vectors = pd.DataFrame([model[word] for word in (model.wv.vocab)])
        vectors['Word'] = list(model.wv.vocab)

        for i in range(len(data)):
            Index.append(i)
        # 'Word'segmentation
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(Index[i])    
            dictionary.extend(i_word)
        Prot_vec['Id'] = dictionary
        
        # word vectors generation
        dictionary=[]
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(texts[i][w])    
            dictionary.extend(i_word)
        Prot_vec['Word'] = dictionary
        
        del dictionary,i_word
        
        Prot_vec = Prot_vec.merge(vectors,on='Word', how='left')
        Prot_vec.columns = ['Id']+['word']+["vec_{0}".format(i) for i in range(0,dims)]
        Prot_vec= Prot_vec.drop('Word',axis=1)
   
        #Protein Sequence Representation

        name = ["vec_{0}".format(i) for i in range(0,dims)]
        Prot_embeddings = pd.DataFrame(Prot_vec.groupby(['Id'])[name].agg('mean')).reset_index()
        Prot_embeddings.columns=["Index"]+["mean_ci_{0}".format(i) for i in range(0,dims)]
        Prot_embeddings.to_csv('Prot_embeddings.csv',index=False)
        
        return Prot_vec,Prot_embeddings

