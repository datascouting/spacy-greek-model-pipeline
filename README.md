The following repository provides all needed information for the support of a Greek model in spaCy that uses as Part of Speech tags classes with morphological features. The tag map can be found in [this](https://github.com/explosion/spaCy/blob/master/spacy/lang/el/tag_map.py) page. The dataset that was used is a source of news from a newspaper called “Makedonia” and is a part of the [clarin](https://www.clarin.gr/) project. The dataset in under the CC – BY – NC – SA licence.
Additional work has been done for the support of Named Entity Recognition in the Greek model. The same annotated source was used for the support of 4 types of named entities (person, organization, location, facility). The annotated dataset with named entities is licenced under the CC – BY – NC – SA licence.
For the creation of the model the train and dev data is provided in proper json format. However, to recreate the dataset from source for use, a number of steps has to be followed.
###Steps
* Step 1: Download and unzip the dataset from [this](https://keg.clarin.gr/resources/browse/modern-greek-texts-corpus-makedonia-newspaper-annotated-by-the-ilsp-lemmatizer/02a9ea6227fc11e6a7b7aa3fc0687644d756918b84cd4f6a88cf2b2f8c0cf3c9/) link.
* Step 2: Move __parsing_sentences.py__ and __parsing_tags.py__ in the archive folder of the extracted dataset.
* Step 3: `python parsing_sentences.py`: Extract the sentences from the dataset. The sentences will be saved in json objects in __sentences.json__.
* Step 4: `python parsing_tags.py`: Extract their pos tags. The __tags.json__ will contain the part of speech tag for all tokens matching the index of the record from __sentences.json__.
* Step 5: Download and unzip the dataset from [this](https://keg.clarin.gr/resources/browse/modern-greek-texts-corpus-makedonia-newspaper-annotated-by-the-grne-tagger/76777cae4c8811e89c6caa3fc6ebde2ce44e9fd17cce43d8ab298aae0c7058fe/) link.
* Step 2: Move __making_entity_list.py__ the archive folder of the extracted dataset.
* Step 6: `python making_entity_list.py`: Create the entity list.
* Step 7: Move __sentences.json__, __tags.json__ and __makedonia_list.txt__ in the same path with the rest of the scripts.
* Step 8: `python edit_entity_list.py`: Edit the entity list.
* Step 9: `python parsing_entitites.py`: Extract the annotated entities from the sentences.
* Step 10: `python convert_to_biluo.py`: Convert the entities to bilou format.
* Step 11: `python convert_to_json_format_and_split_to_train_dev.py`: Convert files in proper json format and split the dataset in train and dev data.
It must be noted that the extracted directories from the upper sources should be located in the same path. Also, configuration has to be done in the init file of lang/el, so the proper tag_map is used.
The model has been trained using as pretrained vectors the Greek, FastText, Common Crawl vectors from [this](https://fasttext.cc/docs/en/crawl-vectors.html) link. As pipelines the POS Tagger and the Entity Recognizer are provided.
