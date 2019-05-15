# -*- coding: utf-8 -*-
import codecs

with codecs.open('makedonia_list.txt','r',encoding='utf-8',errors='ignore') as file:
	entity_dict={}
	for line in file:
		if(len(line.split('    ')) != 2): continue #if not both token and class exist
		entity, entity_class = line.split('    ')
		if(len(entity) < 4): continue #avoid very small entities
		entity_dict[entity] = entity_class

with codecs.open('makedonia_list.txt','w',encoding='utf-8',errors='ignore') as file:
	for entity in sorted(entity_dict, key=len, reverse=True):
		file.write(entity+'    '+entity_dict[entity])
