# -*- coding: utf-8 -*-
import spacy
import codecs
import json
import random

sentences = codecs.open('sentences.json','r',encoding='utf-8',errors='ignore')
tags = codecs.open('tags.json','r',encoding='utf-8',errors='ignore')
entities_biluo = codecs.open('entities_biluo.json','r',encoding='utf-8',errors='ignore')

train_file = codecs.open('train_data.json','w',encoding='utf-8',errors='ignore')
dev_file = codecs.open('dev_data.json','w',encoding='utf-8',errors='ignore')

DATA=[]
nlp=spacy.blank('el')

dict_id=0
while (1):
	print(dict_id)
	try:
		text = json.loads(sentences.readline())["sentence"]
		doc = nlp(text)
		tags_list = json.loads(tags.readline())["tags"].split(' ')
		entities = json.loads(entities_biluo.readline())["entities"]
		if(len(tags_list)!=len(doc)):continue # if bad tokenization
		if(entities==''):continue #if not available entities in sentence
		tokens_list=[]
		for index in range(len(doc)):
			tokens_list.append({"tag": tags_list[index],
			"ner": entities[index], 
			"id": index,
			"orth": str(doc[index])})

		my_list=[{"id": dict_id, "paragraphs": [{"raw": text, "sentences":[{"tokens": tokens_list}]}]}]
		DATA.append(my_list)
		dict_id+=1
	except ValueError:
		break

random.shuffle(DATA)
TRAIN_DATA = DATA[:int(dict_id * 0.7)]
DEV_DATA = DATA[int(dict_id * 0.7):]

for record in TRAIN_DATA:
	train_file.write(json.dumps(record,ensure_ascii=False))
	train_file.write('\n')

for record in DEV_DATA:
	dev_file.write(json.dumps(record,ensure_ascii=False))
	dev_file.write('\n')