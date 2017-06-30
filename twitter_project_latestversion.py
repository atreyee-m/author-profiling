# -*- coding: utf-8 -*-
import re 
import fileinput 
from bs4 import BeautifulSoup
import os
import glob
from os import path
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize,sent_tokenize
from collections import Counter
import pprint 
import cPickle as pickle
import pandas
import itertools
import xml.etree.ElementTree as ET
from collections import defaultdict

dir_path =  r"/scratch/atremukh/essays/essay_text/"
results_dir = r"/scratch/atremukh/essays/features_essays/"
nrc_byemotion = r"/scratch/atremukh/nrc_byemotion/"

#dir_path =  r"/scratch/atremukh/essays/twitter/tweets/"
#results_dir = r"/scratch/atremukh/essays/twitter/features/"

def main():
    print "main func"
    #consolidatefbstat()
    count_pos_types();


def count_pos_types():

    nouns_lst = [] ; adj_lst = [] ; adv_lst = [] ; pronoun_lst = [];word_lst = [];listofwordlist = []
    listofemotions = ['anger','anticipation','disgust','fear','joy','negative','positive','sadness','surprise','trust']
    
    for file_name in glob.glob(os.path.join(dir_path, "*.txt")):
        with open(file_name) as status_file:
            print file_name
            freq_lst = [];#emo_list = []
            anger_list = []
            anticipation_list = []
            disgust_list = []
            fear_list = []
            joy_list = []
            negative_list = []
            positive_list = []
            sadness_list = []
            surprise_list = []
            trust_list = []

            for line in status_file:
                #-----------POS feats-----------
                tagged = pos_tag(word_tokenize(line))
                counts =  Counter([j for i,j in pos_tag(word_tokenize(line.decode('utf-8').strip()))])
                c_NN = counts["NN"] ;   c_NNS = counts["NNS"]   ;   c_NNP = counts["NNP"]   ;   c_NNPS = counts["NNPS"];
                c_RB = counts["RB"]     ;       c_RBR = counts["RBR"]    ;        c_RBS = counts["RBS"];
                c_JJ = counts["JJ"]     ;       c_JJR = counts["JJR"]    ;        c_JJS = counts["JJS"];
                c_PRP = counts["PRP"]   ;   c_personalPRP = counts["PRP$"];
                #print c_NN+c_NNS+c_NNP+c_NNPS , c_JJ+c_JJR+c_JJS, c_RB+c_RBR+ c_RBS, c_PRP+c_personalPRP
                nouns = c_NN+c_NNS+c_NNP+c_NNPS; nouns_lst.append(nouns)
                adj = c_JJ+c_JJR+c_JJS ; adj_lst.append(adj) ;    
                adv = c_RB+c_RBR+c_RBS; adv_lst.append(adv);
                pronouns = c_PRP+c_personalPRP; pronoun_lst.append(pronouns)
               
                #just splitting the line into words
                parts = line.split(' ');
                #-----------stopwords-----------------
                freq = stopwords_frequency(parts);
                freq_lst.append(freq)
                #-----------NRC emotions and positive and negative sentiments-----------------
                #emotions(parts) #do not open this
                         
                anger = count_emotion(parts,'anger')
                anger_list.append(anger)
                 
                anticipation = count_emotion(parts,'anticipation')
                anticipation_list.append(anticipation)
                 
                disgust = count_emotion(parts,'disgust')
                disgust_list.append(disgust)
                 
                fear = count_emotion(parts,'fear')
                fear_list.append(fear)
                 
                joy = count_emotion(parts,'joy')
                joy_list.append(joy)
                 
                negative = count_emotion(parts,'negative')
                negative_list.append(negative)
                 
                positive = count_emotion(parts,'positive')
                positive_list.append(positive)
                 
                sadness = count_emotion(parts,'sadness')
                sadness_list.append(sadness)
                 
                surprise = count_emotion(parts,'surprise')
                surprise_list.append(surprise)
                 
                trust = count_emotion(parts,'trust')
                trust_list.append(trust)
                 
            #print emo_list
#             print "anger_list         ",anger_list             
#             print "anticipation_list", anticipation_list     
#             print "disgust_list     ",    disgust_list         
#             print "fear_list         ",fear_list             
#             print "joy_list         ",    joy_list             
#             print "negative_list     ",negative_list         
#             print "positive_list     ",positive_list         
#             print "sadness_list     ",    sadness_list         
#             print "surprise_list     ",surprise_list         
#             print "trust_list        ",trust_list            
 

            
            #----------constructing the final feature----------
            finalstring = str(sum(nouns_lst))+','+str(sum(adj_lst))+','+str(sum(adv_lst))+','+str(sum(pronoun_lst))+','+str(sum(freq_lst))+','+str(sum(anger_list))+','+str(sum(anticipation_list))+','+str(sum(disgust_list))+','+str(sum(fear_list))+','+str(sum(joy_list))+','+str(sum(negative_list))+','+str(sum(positive_list))+','+str(sum(sadness_list))+','+str(sum(surprise_list))+','+str(sum(trust_list))
            #finalstring = str(sum(anger_list))+','+str(sum(anticipation_list))+','+str(sum(disgust_list))+','+str(sum(fear_list))+','+str(sum(joy_list))+','+str(sum(negative_list))+','+str(sum(positive_list))+','+str(sum(sadness_list))+','+str(sum(surprise_list))+','+str(sum(trust_list))
            #print finalstring
            #----------writing to the result file----------
            results_file = "%s%s.txt"%(results_dir, os.path.splitext(os.path.basename(file_name))[0])
            with open(results_file, 'a') as fp:    
                fp.write(finalstring)


def emotions(lst,i):
    #print "emotions!!!!"
    d = defaultdict(list)
    #print lst
    emotionfilename = str(i+".txt")
    f = os.path.join(nrc_byemotion, emotionfilename)
    
    with open(f) as inf:
        for line in inf:
            k,v = line.strip().split()
            d[k].append(int(v))
    #print d
    return d

def count_emotion(lst,i):
    emo_dict = {};count = 0;words_found = [];emo_val =[];empty=0;nonempty = 0;ifwordnotfound = [0]
    lwrlst = [x.lower() for x in lst]
    #print lst,lwrlst
    emo_dict = emotions(lwrlst,i)
    #print emo_dict
    #print lst
    for l in lwrlst:
        if l in emo_dict.keys():
            emo_val.append(emo_dict.get(l))
            words_found.append(l)
        else:
            #print "did not find"
            emo_val.append(ifwordnotfound)
    #print lwrlst,words_found,emo_val
    x = [sum(i) for i in zip(*emo_val)]
    
    if len(x) == 0:
        return empty
    else:
        nonempty = x.pop()
        #print words_found,nonempty
        return nonempty
    

def stopwords_frequency(lst):
    #print lst
    eachstopwordcount=0;stopwordlst = []
    for stopword in stopwords.words('english'):
        if stopword in lst:
            #print "inside if"
            eachstopwordcount+=1
            #print eachstopwordcount
        #print "for loop level",eachstopwordcount 
    return eachstopwordcount

def consolidatefbstat():
    print"x"
    listofuserids = []
    with open('mypersonality_final.csv') as inf:
        for line in inf:
            eachcol=line.split(',')
            listofuserids.append(eachcol[0])
    x = set(listofuserids)
    #print x,len(x)
    for item in x:
        #print item.strip('"')
        consolidateFB(item.strip('"'))
        
def consolidateFB(item):
    #with open('mypersonality_final.csv') as inf:
    with open('FB_authorid_status.txt') as inf:
        for line in inf:
            eachcol=line.split('\t')
            #print eachcol[0]
            userid = eachcol[0].strip('"')
            if(userid == item):
                filename = "fbstat_"+str(item)+".txt"
                f = open(filename,'a')
                f.write(eachcol[1])
                f.close()
               
                

    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()