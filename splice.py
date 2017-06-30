import urllib, urllib2
from xml.dom import minidom
import os
import glob
from os import path
from bs4 import BeautifulSoup
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
#create url

def main():

#--Change the values of these variables
#hedgeVerb hedgeConj hedgeAdj hedgeModal hedgeAll numDisfluencies disfluencyRatio numInterjections interjectionRatio numSpeculate speculateRatio Expressivity numIgnorance ignoranceRatio Pausality questionCount questionRatio hedgeUncertain
#--Positive Self Evaluation/-ve self evaluation
#iCanDoIt doKnow posSelfImage iCantDoIt dontKnow negSelfImage
#--influence
#numImperatives suggestionPhrases inflexibility contradict totalDominance dominanceRatio numAgreement agreementRatio
#--deference
#askPermission seekGuidance totalSubmissiveness submissivenessRatio
#--whissel    
#Imagery Pleasantness Activation
#--sentence complexity
#avgWordLength avgSentenceLength numSyllables avgSyllablesPerWord numWordsWith3OrMoreSyllables rateWordsWith3OrMoreSyllables numWordsWith6OrMoreChars rateWordsWith6OrMoreChars numWordsWith7OrMoreChars rateWordsWith7OrMoreChars LexicalDiversity complexityComposite    
#pastTense pastTenseRatio presentTense presentTenseRatio 
#SWNpositivity SWNnegativity SWNobjectivity
#numChars numCharsMinusSpacesAndPunctuation numWords numSentences numPunctuation
    

    
    d = {}
    with open("rem_splice.txt") as inf:
        for line in inf:
            k,v = line.split('\t')
            d[k]= v

    
    for k, v in d.iteritems():
        splice_feat(k, v)
    
def splice_feat(k,v):
    #dir_path =  r"/scratch/atremukh/tweets/"
    #results_dir = r"/scratch/atremukh/twitter-splice-features/"    
    theCues_1 =  'numImperatives suggestionPhrases inflexibility contradict totalDominance dominanceRatio numAgreement agreementRatio'
    
    dir_path = r"/scratch/atremukh/essays/essay_text/"
    results_dir = r"/scratch/atremukh/essays/splice_feat_essays/"
    
    feats = k.strip().replace('\"','')
    theCues = v.replace('\"','')
    #print theCues_1 ,theCues
    
    
    for fileName in glob.glob(os.path.join(dir_path, "*.txt")):
           
       
    #fileName = r'/scratch/atremukh/fb_stat_by_usrid/fbstat_330abbccd3c0ad0fdb0cbe815599bd4f.txt'   # Put the name of the file you wish to analyze here
    # Put list of cues here(theCues) in a string separated by spaces
                   
   
# Don't change this section
# ======================================
        url = 'http://splice.cmi.arizona.edu/SPLICE/post/postargs/'
        theFile = open(fileName).read()
        data = 'text=' + theFile + '&cues=' + theCues
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
# ======================================
   
# This is your variable that holds the results from SPLICE
        the_data = response.read()
        #print the_data
           
        soup = BeautifulSoup(the_data,"lxml")
        text = soup.get_text(',').encode('utf-8')
        results_file = "%s%s%s.txt"%(results_dir,feats, os.path.splitext(os.path.basename(fileName))[0])
        with open(results_file, 'a') as fp:    
            fp.write(text)
         
  
         
if __name__ == "__main__":
    main() 