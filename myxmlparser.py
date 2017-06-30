import re 
import fileinput 
from bs4 import BeautifulSoup
import os
import glob
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

def main():
    tree = ET.parse('fbstat_9e7ebc8082b0e7e92e7aedd3ba562d84.txt')
    root = tree.getroot()
    d = {}
    print root
    
    
# def xmlparse():
#     tree = ET.parse('mypersonality_status.txt.out')
#     root = tree.getroot()
#     d = {}
#     
#     for child in root:
#         for grandchild in child:
#             for greatgrandchild in grandchild:
#                 #if 'sentiment' and 'sentimentValue' in greatgrandchild.attrib.keys():
#                 print greatgrandchild.attrib['sentiment'], greatgrandchild.attrib['sentimentValue']
    
    
if __name__ == "__main__":
    main() 