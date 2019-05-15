# -*- coding: utf-8 -*-
import codecs
import json

entity_value=[]
entity_class=[]

with codecs.open('makedonia_list.txt','r',encoding='utf-8',errors='ignore') as file:
    for line in file:
        pair=line.split('    ')
        entity_value.append(pair[0])
        entity_class.append(pair[1].split('\n')[0])

#remove newline
entity_class=entity_class[:-1]
entity_value=entity_value[:-1]

#replace classes in spaCy's format
entity_class = [e.replace('ORGANIZATION', 'ORG') for e in entity_class]
entity_class = [e.replace('LOCATION', 'LOC') for e in entity_class]
entity_class = [e.replace('FACILITY', 'FAC') for e in entity_class]

entities=codecs.open('entities.json','w',encoding='utf-8',errors='ignore')

with codecs.open('sentences.json','r',encoding='utf-8',errors='ignore') as file:
    num=0
    for line in file:
        print(num)
        sentence=json.loads(line)['sentence']
        entity_lists=[] #list with all entity values available in sentence
        final_record=[] #records that are saved in entities.json
        
        for index in range(len(entity_value)): # check all entities from makedonia_list.txt
            entity=entity_value[index]
            if entity in sentence:
                begin_entity=sentence.find(entity)
                end_entity=begin_entity+len(entity)
                entity_lists_index=0
                entity_conflict=False # whether the token is used in another entity to avoid wrong processing (example: "Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης", entity_conflict: "Δήμος Θεσσαλονίκης")
                while(entity_lists_index<len(entity_lists)):
                    if (bool(set(range(begin_entity,end_entity)) & set(entity_lists[entity_lists_index]))): # if range of entity is located in entity range
                        entity_conflict=True
                        break
                    entity_lists_index+=1
                if(not entity_conflict): # correct named entity
                    entity_lists.append(range(begin_entity,end_entity))
                    final_record.append((begin_entity,end_entity,entity_class[index]))

        if(entity_lists==[]):
            my_dict={"entities":""}
        else:
            my_dict={"entities":str(final_record)}

        json.dump(my_dict,entities,ensure_ascii=False)
        entities.write('\n')
        num+=1
