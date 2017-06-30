from __future__ import division
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
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.feature_extraction.text import TfidfVectorizer
import pprint
from decimal import Decimal, getcontext

#awk -F" " '{print >  "topicfile_"$3}' final_FBfilenameWordTopicProbability.txt -- split based on topics
dir_path =  r"/scratch/atremukh/fb_stat_by_usrid/"


def main():
#     print "main func"
#     
#     corpus = []
#     
#     with open(r'/N/u/atremukh/Karst/author_profiling/auth_prof_project/fb_stat_by_usrid/fbstat_2badb47503a98766c89e266d1130969a.txt') as inf:
#         for line in inf:
#             corpus.append(line)
#     #print corpus
#         
#     vectorizer = TfidfVectorizer(min_df=1)
#     X = vectorizer.fit_transform(corpus)
#     idf = vectorizer.idf_
#     pprint.pprint(dict(zip(vectorizer.get_feature_names(), idf)))
##############################################################    
    calculatetopicfeatures()
        
#     with open(r'/scratch/atremukh/7SWfb_stat_by_usrid-topic-state.txt') as inf:
#         probability =0
#         for line in inf:
#             splits = line.strip().split(' ')
#             #print splits[1],splits[4],splits[5]
#             filename = splits[1]
#             topic = splits[5]
#             probability = find_probab(filename,topic)
#             print filename,splits[4],topic,probability
    #find_probab(filename,topic)   
##############################################################  
def calculatetopicfeatures():
    #print "x"
    #print os.path.basename('/scratch/atremukh/fb_stat_by_usrid/fbstat_fc1c9fb6c64740edcbbf8cfe9dde8b02.txt')
    words = 0
    lst = [];
    for file_name in glob.glob(os.path.join(dir_path, "*.txt")):
        with open(file_name) as inf:
            lis = []
            
            for line in inf:
                re.findall(r"[\w']+", line)
                lst.append(re.findall(r"[\w']+", line))
            #print lst,"\n"
            #print list(itertools.chain(*lst)),"\n"
            wordcount=Counter(list(itertools.chain(*lst)))
            #print wordcount,"\n"
    #     for wc in open(r"/scratch/atremukh/fb_stat_by_usrid/fbstat_fc1c9fb6c64740edcbbf8cfe9dde8b02.txt").read().split():
    #         words+=1
        totalwords=0
        for i in lst:
            totalwords += len(i)
        #print totalwords
        

        
        for key,value in wordcount.items():
            #print key, value, float(value/totalwords)
            p_WgivenS = float(value/totalwords)
            lis.append(topicfeat(key, value,os.path.basename(file_name),p_WgivenS))
                
        print os.path.basename(file_name),"topic 0",sum(filter(None,lis))
    
    
def topicfeat(k,v,f,p_WgivenS):
    #print "topicfeat"
    #print k#,p_WgivenS
    
    falseval = 0.0
    with open(r"/scratch/atremukh/final_FBfilenameWordTopicProbability.txt") as inf:
        #p_TgivenW_0=[]
        for line in inf:
            splits = line.split(' ')
            #print splits[0],f
            #print splits[1],k
            
            if(splits[0] == f and splits[1] == k):
                #print k,v,f,splits[2], splits[3],p_WgivenS
                #p_TgivenW_0 = []
#                 p_TgivenW_0_each=0
#                 
                if(splits[2] == "0"):                 
                    p_TgivenW_0_each = float(splits[3])*p_WgivenS
                    return p_TgivenW_0_each
                else:
                    return falseval
                
            
                
                    
                
                
                
                    #p_TgivenW_0.append(p_TgivenW_0_each)
#                 else:
#                     p_TgivenW_0.append(0)
#                 print  p_TgivenW_0  
# def prob_topic_word():
#     with open(r"/scratch/atremukh/fb_filenames.txt") as inf:
#         for line in inf:
#             probab_topic_word(line)
            
     
def find_probab(filename,topic):
    
    #filename = 'file:/u/atremukh/mallet-2.0.7/fb_stat_by_usrid/fbstat_fc1c9fb6c64740edcbbf8cfe9dde8b02.txt'
    #topic = '0'
    #print filename,topic
    
    with open(r'/scratch/atremukh/newdoctopics.txt') as inf:
        for line in inf:
            #print line
            parts = line.strip().split('\t')
            #topicinfile = parts[2::2]
            #print parts
            #print parts[0],filename
            tmp = parts[0]
            tmp1 = tmp.split(":")
            #print tmp1[1],filename
            if tmp1[1] == filename:
                #print filename
                if str(topic) in parts:
                    #print topic
                    #print filename, topic, parts[parts.index(topic) + 1]
                    return parts[parts.index(topic) + 1]         
            
            
    
if __name__ == "__main__":
    main() 
