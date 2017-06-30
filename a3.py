# -*- coding: utf-8 -*-
import re 
import fileinput 
from bs4 import BeautifulSoup
import os
import glob


output_dir = "/N/u/atremukh/Karst/author_profiling/A3/outputdir"  

# for line in fileinput.input():
#     #print line
#     print fileinput.filename()

    
    


# def process_one_file(f):     
#     
#     soup=BeautifulSoup(open(f),'lxml')      
#     #print(soup.get_text()).encode('utf-8')
#     fw = open("out.txt","w")
#     fw.write(soup.get_text().encode('utf-8'))
#     fw.close
#

def main(): 
    #f = "/N/u/atremukh/Karst/author_profiling/A3/pan16-author-profiling-training-dataset-2016-04-25/05f97ea55282c4f81fce6fa5751a7ef4.xml"
    dir_path =  r"/N/u/atremukh/Karst/author_profiling/A3/sendtokarst/"
    results_dir = r"/N/u/atremukh/Karst/author_profiling/A3/extract/"
    #dir_path =  r"/N/u/atremukh/Karst/author_profiling/A3/"
    #results_dir = r"/N/u/atremukh/Karst/author_profiling/A3/test/"
    for file_name in glob.glob(os.path.join(dir_path, "*.xml")):
        with open(file_name) as xml_file:
            soup = BeautifulSoup(xml_file,"lxml")
            results_file = "%s%s.txt"%(results_dir, os.path.splitext(os.path.basename(file_name))[0])
            with open(results_file, 'w') as fp:
                text = soup.get_text().encode('utf-8')
                #print text
                URLless_string = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?������]))', '', text)
                #fp.write(soup.get_text().encode('utf-8'))
                URLless_string = re.sub(r']]>','',URLless_string)
                fp.write(URLless_string)

    
    
    #process_one_file(f)

if __name__ == "__main__":
    main()


# def process_one_line(line):     
#     p = re.search('CDATA\[(.*)\]]',line)     
#     if p:         
#         data = p.group(1)         
#         # for now:         
#         data = re.sub('<.*?>','',data)         
#         # character substitutions:         
#         data = re.sub("&#39;","'",data)         
#         data = re.sub("&amp;","&",data)         
#         data = re.sub("&quot;",'"',data)         
#         data = re.sub("&nbsp;"," ",data)         
#         data = re.sub("&lt;","<",data)         
#         data = re.sub("&gt;",">",data)         
#         return data     
#     return None
#     
# def main_one():          
#     for line in fileinput.input():         
#         print line
#         line = line.rstrip()         
#         line = process_one_line(line)         
#         if line:             
#             print(line+'\n')    
# 
# main_one()

