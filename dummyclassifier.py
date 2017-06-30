import re 
import fileinput 
from bs4 import BeautifulSoup
import os
import glob
from os import path
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter
import pprint 
import cPickle as pickle
import pandas
import itertools
import xml.etree.ElementTree as ET
from collections import defaultdict
#scikit-learn
#from sklearn.feature_extraction import DictVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.datasets import fetch_20newsgroups
#from sklearn.datasets import load_iris

import numpy as np
from numpy import array
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
import scipy
from sklearn.linear_model import SGDClassifier
import sklearn.linear_model.tests.test_randomized_l1
from sklearn import metrics
from sklearn.dummy import DummyClassifier
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
import csv
from sklearn import tree
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest,chi2

#from sklearn.feature_selection import SelectFromModel
#import sklearn.feature_selection

#  extraversion
#  neuroticism
#  agreeableness
#  conscientiousness
#  openness

def main():
    
    ###############################################################################################################
    pretrainfeat = open(r"/scratch/atremukh/classfierfiles/essays/essay_features_full.txt")
    pretraintarget = open(r"/scratch/atremukh/classfierfiles/essays/EXT_essay_target_full.txt")
     
    pretestfeat = open(r"/scratch/atremukh/classfierfiles/facebook/all_features.txt")
    pretesttarget = open(r"/scratch/atremukh/classfierfiles/facebook/extraversion-allFiles-target.txt") 
    
    
###############################################################################################################
    
    #predefined train
#     pretrainfeat = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/trainfeat.txt")
#     pretraintarget = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/agreeablenessTrainTargetClass.txt")
#      
#     pretestfeat = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/testfeat.txt")
#     pretesttarget = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/neuroticismTestTargetClass.txt") 
    #print pretesttarget
###############################################################################################################     
    trainfeat = readFile(pretrainfeat)
    traintarget = newreadfile(pretraintarget)
#       
    testfeat = readFile(pretestfeat)
    testtarget = newreadfile(pretesttarget)
    
    #print trainfeat;print "\n"
    trainfeat_np = np.array(trainfeat,dtype=float)#.astype(np.float)
    #print trainfeat_np
    traintarget_np = np.array(traintarget)
     #print traintarget_np
     
    testfeat_np = np.array(testfeat).astype(np.float)
    #print testfeat_np
    testtarget_np = np.array(testtarget)
    #print testtarget_np
      
    #trainfeat_np,traintarget_np,testfeat_np,testtarget_np = train_test_split()
     
     
###############################################################################################################
    #cross validation
    #pre_features = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/count-emo/emotionfeatures.txt")
#     pre_features = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/all_features.txt")
#     pre_target = open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/conscientiousness-allFiles-target.txt") 
#     
#     
#     prenp_features = readFile(pre_features)
#     prenp_target = newreadfile(pre_target)
#     
#     features = np.array(prenp_features).astype(np.float)
#     target = np.array(prenp_target).astype(np.int)
#     #target = converttargetformultilabel()
#     #print target
#     trainfeat_np, testfeat_np, traintarget_np, testtarget_np = train_test_split(features,target, test_size = 0.2, random_state = 0)
    ###############################################################################################################
#     clf = RandomForestClassifier(n_estimators = 50)
#     #decision_tree = decision_tree.fit(trainfeat_np,traintarget_np)
#     scores = cross_val_score(clf,features,target,cv = 5)
#     print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    ###############################################################################################################
    #FEATURE SELECTION
    #TREE BASED
#     etc =  ExtraTreesClassifier()
#     etc = etc.fit(trainfeat_np,traintarget_np)
#     model = SelectFromModel(clf, prefit=True)
#     features_new = model.transform(features)
#     
#     for i in range(5,79):
#         print i
#         features_new = SelectKBest(chi2, k=i).fit_transform(features, target)
#     
#         clf = DummyClassifier(strategy='most_frequent',random_state=0)
#         scores = cross_val_score(clf,features_new,target,cv = 5)
#         print("Accuracy dummy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))  
#         
#         gnb = GaussianNB()
#         scores = cross_val_score(gnb,features_new,target,cv = 5)
#         print("Accuracy GNB: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)) 
#         
#         svm = SVC(kernel='linear', C=1)
#         scores = cross_val_score(svm,features_new,target,cv = 5)
#         print("Accuracy GNB: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)) 
    
    
    ###############################################################################################################
     
    #dummy
 
#     clf = DummyClassifier(strategy='most_frequent',random_state=0)
#     clf.fit(trainfeat_np,traintarget_np)
#     print clf.score(testfeat_np, testtarget_np)
#     #scores = cross_val_score(clf,features,target,cv = 5)
# #    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
#        
#     #SVM
#     clf1 = SVC(kernel='linear', C=1)
#     clf1.fit(trainfeat_np,traintarget_np)
#     print clf1.score(testfeat_np, testtarget_np)
# #    scores = cross_val_score(clf1,features,target,cv = 5)
# #    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
#        
#     clf1_2 = SVC(kernel='rbf', C=1)
#     clf1_2.fit(trainfeat_np,traintarget_np)
# #    print clf1_2.score(testfeat_np, testtarget_np)
# #    scores = cross_val_score(clf1_2,features,target,cv = 5)
# #    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
       
    clf2 = GaussianNB()
    clf2.fit(trainfeat_np,traintarget_np)
    print clf2.score(testfeat_np, testtarget_np)
      
#     forest = RandomForestClassifier(n_estimators = 50)
#     forest.fit(trainfeat_np,traintarget_np)
#     print forest.score(testfeat_np, testtarget_np)
#    scores = cross_val_score(clf2,features,target,cv = 5)
#    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)) 
      
#      
###############################################################################################################




# def converttargetformultilabel():
#     with open(r"/N/u/atremukh/Karst/author_profiling/auth_prof_project/FB-features/fullstat_target.txt") as csvfile:
#         csvreader = csv.reader(csvfile)
#         lst1 = []
#         for row in csvreader:
#             y = np.array(row).astype(int)
#             lst1.append(y)
#             x = np.array(lst1)
#         return x
        
def newreadfile(f):
    targets = f.readlines()
    lst=[]
    for i in targets:
        lst.append(int(i.rstrip()))
    #print lst
    return lst
        
#def usingBagOfWords():  
              
    
            
def readFile(fileReader):
    lines = fileReader.readlines()
    
    listMatrix = []
    for line in lines:
        linelist = line.strip('"').split(',')
        listMatrix.append(linelist)
    #print listMatrix
    #print "\n"
    return listMatrix
        
        
    
    

if __name__ == "__main__":
    main() 