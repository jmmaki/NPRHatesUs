#pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
#from here is how to download, install and connect MongoDB to the python
#this must be in terminal
#python -m pip install pymongo
#python - m pip install "pymongo[srv]"

#in python env
import pymongo
from pymongo import MongoClient
from pprint import pprint
#connect to MDB
#in terminal:
#python mongodbtest.py

import spacy
#spacy download en_core_web_sm
nlp=spacy.load('en_core_web_sm')
#from spacy.tokens import Doc
import json
import nltk.tokenize
from nltk.tokenize import sent_tokenize
##import re
nltk.download('punkt')
#setup database
client=MongoClient('mongodb+srv://JMaki:<password>@nprhatesus.yghzs.mongodb.net/npr?retryWrites=true&w=majority')
db=client.newsarts

#recurse through subdirs and files
import os
directory= '/home/ubuntu/data/88260'
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        h = open(directory+'/'+filename )
        data=json.load(h)
        article= data.get('story_text')
        sentences = sent_tokenize(article)
        keywords = ["professor", 'researcher']
        keymatch=[s for s in sentences if any(k in s for k in keywords)]
        #keymatch.append("Robert is a man")
        for string in keymatch:
            new=str(string)
            doc=nlp(new)
            for ent in doc.ents:
                if ent.label_=='PERSON':
                    resultdic=data.copy()
                    resultdic.pop("story_tags")
                    resultdic.pop("story_text")
                    #print(ent.text, ent.label_)
                    result= (ent.text,ent.label_)
                    resultdic.update({"name": ent.text, "label": ent.label_,"sent match": keymatch})
                    x = db.newsarts.insert_one(resultdic)
                    print('done')
                else:
                    continue
        h.close()
    else:
        break
