# -*- coding: utf-8 -*-
import spacy
import codecs
import json
from ast import literal_eval

entities_biluo = codecs.open('entities_biluo.json','w',encoding='utf-8',errors='ignore')

nlp=spacy.blank('el')
with codecs.open('entities.json','r',encoding='utf-8',errors='ignore') as ent_file, codecs.open('sentences.json','r',encoding='utf-8',errors='ignore') as sent_file:
	for sent_line in sent_file:
		doc = nlp(json.loads(sent_line)["sentence"])
		entities = json.loads(ent_file.readline())["entities"]
		
		if(entities):
			my_dict = {"entities":spacy.gold.biluo_tags_from_offsets(doc, literal_eval(entities))}
		else:
			my_dict = {"entities":""}
		
		json.dump(my_dict,entities_biluo,ensure_ascii=False)
		entities_biluo.write('\n')