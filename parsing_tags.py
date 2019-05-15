# -*- coding: utf-8 -*-
import codecs
from lxml import etree
import json

names={'types':"http:///gr/ilsp/types.ecore",'xmi':"http://www.omg.org/XMI"}
n={'cas':"http:///uima/cas.ecore",'xmi':"http://www.omg.org/XMI"}

tags=codecs.open('tags.json','w',encoding='utf-8',errors='ignore') #file to write sentences

for i in range(1696):
    file='split'+str(i)+'_makedonia.txt'
    print(file)
    article=etree.parse(file)
    with codecs.open(file,'r',encoding='utf-8',errors='ignore') as file:
        sofas=article.xpath("cas:Sofa/@sofaString",namespaces=n)[0] #news text
        begin_tokens=article.xpath("//types:Token/@begin",namespaces=names)
        end_tokens=article.xpath("//types:Token/@end",namespaces=names)
        sent_ord=article.xpath("//types:Token/@sentOrd",namespaces=names) #index of token in sentence
        num_sentences=len(article.xpath("//types:Sentence/@end",namespaces=names))
        pos_tokens_id=article.xpath("//types:Token/@posTag",namespaces=names) #pos id to locate the class
        index=0
        for num in range(num_sentences):
            sentence=''            
            while(1):
                tag_value=(article.xpath("//types:POSTag[@xmi:id="+pos_tokens_id[index]+"]/@value",namespaces=names))[0]
                sentence=sentence+tag_value+' '
                index=index+1
                if(len(sent_ord)==index or sent_ord[index]=='1'):
                    if(sentence[:-1]!='ENUM PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT PUNCT'): #ignore noise
                        my_dict={"tags": u''.join(sentence[:-1])}
                        json.dump(my_dict,tags,ensure_ascii=False)
                        tags.write('\n')
                    break