# SPVec
Codes and datasets for "SPVec: A Word2vec-inspired feature representation method for Drug-Target Interaction Prediction"
# Introduction
Drug discovery is an academical and commercial process of global importance. Accurate identification of drug-target interactions (DTIs) can significantly facilitate the drug discovery process. Compared to the costly, labour-intensive and time-consuming experimental methods, machine learning (ML) plays an ever-increasingly important role in effective, efficient and high-throughput identification of DTIs. However, upstream feature extraction methods require tremendous human resources and expert insights, which limited the application of ML approaches.Inspired by the unsupervised representation learning methods like Word2vec, we proposed SPVec, a novel way to automatically represent raw data such as SMILES strings and protein sequences into continuous, information-rich and lower-dimensional vectors, so as to avoid the sparseness and bit collisions from the cumbersomely manually extracted features. SPVec illustrated that the similar compounds or proteins occupy similar vector space, which indicated that SPVec not only encodes compound substructures or protein sequences efficiently, but also implicitly reveals some important biophysical and biochemical patterns. SPVec can provide an effective and efficient way to discover reliable DTIs, which would be beneficial for drug reprofiling.
# Installation and usage
 `pip install git+https://github.com/dqwei-lab/SPVec`
 
This method developed with Python 3.7, please make sure all the dependencies are installed, which is specified in `requirements.txt`.

'''from SPVec import SMILES2Vec
from SPVec import ProtVec
'''
First line imports functions to generate continuous feature vectors from small molecular drugs, and second line imports functions to generate continuous feature vectors from protein targets.

# Codes and datasets
`datasets_construction.py` are codes for data preprocessing and datasets construction.  
`feature_reprensentation.py` are codes for SPVec implemention  
`models_training.py` are codes for parameters tuning and models training.  
raw data can be downloaded from https://www.bindingdb.org/bind/chemsearch/marvin/SDFdownload.jsp?all_download=yes  and https://www.drugbank.ca/release

# References
SPVec: A Word2vec-inspired feature representation method for Drug-Target Interaction Prediction

