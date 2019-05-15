# -*- coding: utf-8 -*-
import codecs
from lxml import etree

names={'types':"http:///gr/ilsp/types.ecore",'xmi':"http://www.omg.org/XMI"}
n={'cas':"http:///uima/cas.ecore",'xmi':"http://www.omg.org/XMI"}

entities=codecs.open('makedonia_list.txt','w',encoding='utf-8',errors='ignore')

for i in range(1696):
    print(i)
    file_pos='../../755b062e73e111e5b5c6aa3fc8d33ad892be00b397914b38a887df7ee45fb3f9/archive/split'+str(i)+'_makedonia.txt' # dataset with part of speech tags
    file_ner='split'+str(i)+'_makedonia.txt.tagged' # dataset with named entities
    article_pos=etree.parse(file_pos)
    article_ner=etree.parse(file_ner)
    with codecs.open(file_pos,'r',encoding='utf-8',errors='ignore') as file_pos:
        with codecs.open(file_ner,'r',encoding='utf-8',errors='ignore') as file_ner:
            sofas=article_pos.xpath("cas:Sofa/@sofaString",namespaces=n)[0] #news text
            begin_tokens=article_ner.xpath("//Annotation[@Type='LOCATION' or @Type='ORGANIZATION' or @Type='FACILITY'or @Type='PERSON']/@StartNode",namespaces=names)
            end_tokens=article_ner.xpath("//Annotation[@Type='LOCATION' or @Type='ORGANIZATION' or @Type='FACILITY'or @Type='PERSON']/@EndNode",namespaces=names)   
            entity_tokens=article_ner.xpath("//Annotation[@Type='LOCATION' or @Type='ORGANIZATION' or @Type='FACILITY'or @Type='PERSON']/@Type",namespaces=names)          
            for index in range(len(begin_tokens)):
                entities.write(sofas[int(begin_tokens[index]):int(end_tokens[index])]+'    '+entity_tokens[index])
                entities.write('\n')
