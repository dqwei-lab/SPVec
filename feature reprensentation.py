"""
#filename:feature reprensentation.py
# - * - coding:UTF - 8 -* -
#! /usr/bin/python
__author__ = "Yu-Fang Zhang" 
"""
import pandas as pd
import numpy as np
import gensim 
import jieba
from gensim.models import Word2Vec 
import random 
from sklearn.decomposition import IncrementalPCA
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import os 
import random
import seaborn as sns 

os.chdir('E:\\')

class SPVec:

    def __init__(self,filename):
        self.filename = filename
   
    def read_data(self):
        data=pd.read_csv(self.filename)
        return data

    def word2vec(self,dims,window_size,negative_size):
        word_vec = pd.DataFrame()
        dictionary=[]
        Index = []
        data=self.read_data()
        texts = [[word for word in re.findall(r'.{3}',document)] for document in list(data)]
        model = Word2Vec(texts,size=dims,window=window_size,min_count=1,negative=negative_size,sg=1,sample=0.001,hs=1,workers=4)
        vectors = pd.DataFrame([model[word] for word in (model.wv.vocab)])
        vectors['Word'] = list(model.wv.vocab)

        for i in range(len(data)):
            Index.append(i)
        # Word segmentation
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(Index[i])    
            dictionary.extend(i_word)
        word_vec['Id'] = dictionary
        
        # word vectors generation
        dictionary=[]
        for i in range(len(texts)):
            i_word=[]         
            for w in range(len(texts[i])):
                i_word.append(texts[i][w])    
            dictionary.extend(i_word)
        word_vec['Word'] = dictionary
        del dictionary,i_word
        word_vec = word_vec.merge(vectors,on='Word', how='left')
        #word_vec = word_vec.drop('Word',axis=1)
        word_vec.columns = ['Id']+['word']+["vec_{0}".format(i) for i in range(0,dims)]

        return word_vec

    #Molecular Structure and Protein Sequence Representation
    def feature_embeddings(self,dims):
        word_vec = self.word2vec(dims,window_size,negative_size)
        word_vec=word_vec.drop('Word',axis=1)
        name = ["vec_{0}".format(i) for i in range(0,dims)]
        feature_embeddings = pd.DataFrame(word_vec.groupby(['Id'])[name].agg('mean')).reset_index()
        feature_embeddings.columns=["Index"]+["mean_ci_{0}".format(i) for i in range(0,dims)]
        return feature_embeddings


if __name__=='__main__':
    print ("Molecular Structure and Protein Sequence Continuous Representation")
    print ("*********************************************")
    try:
        
        protein_data=SPVec.read_data()
        drug_data=SPVec.read_data()
        protein_seq=protein_data['proteinseq']
        drug_Smi=drug_data['SMILES']
        drug_vec=SPVec.word2vec(100,6,12,15)
        prot_vec=SPVec.word2vec(100,3,12,15)
        prot_embeddings = Word2vec.feature_embeddings(100)
        drug_embeddings =Word2vec.feature_embeddings(100)
        prot_embeddings['proteinseq']=protein_seq
        drug_embeddings['smiles']=drug_Smi
        prot_embeddings.to_csv('protein_embeddings.csv',index=False)
        drug_embeddings.to_csv('drug_embeddings.csv',index=False)
    except ImportError:
        print ('Molecular Structure and Protein Sequence Continuous Representation error! ')

    finally:
        print ('******Molecular Structure and Protein Sequence Continuous Representation finished!*********')

