The following repository provides all needed information for the support of a Greek model in spaCy that uses as Part of Speech tags classes with morphological features. The tag map can be found in [this](https://github.com/explosion/spaCy/blob/master/spacy/lang/el/tag_map.py) page. The dataset that was used is a source of news from a newspaper called “Makedonia” and is a part of the [clarin](https://www.clarin.gr/) project. The dataset in under the CC – BY – NC – SA licence.
Additional work has been done for the support of Named Entity Recognition in the Greek model. The same annotated source was used for the support of 4 types of named entities (person, organization, location, facility). The annotated dataset with named entities is licenced under the CC – BY – NC – SA licence.
For the creation of the model the train and dev data is provided in proper json format. However, to recreate the dataset from source for use, a number of steps has to be followed.

* Step 1: Download and unzip the dataset with the pos tags from [this](https://keg.clarin.gr/resources/browse/modern-greek-texts-corpus-makedonia-newspaper-annotated-by-the-ilsp-lemmatizer/02a9ea6227fc11e6a7b7aa3fc0687644d756918b84cd4f6a88cf2b2f8c0cf3c9/) link and move the unzipped folder in the same path with the scripts.
* Step 2: `python parsing_sentences.py`: Extracts the sentences from the dataset. The sentences will be saved in json objects in __sentences.json__.
* Step 3: `python parsing_tags.py`: Extracts their pos tags. The __tags.json__ will contain the part of speech tag for all tokens matching the index of the record from __sentences.json__.
* Step 4: Download and unzip the dataset with the named entities from [this](https://keg.clarin.gr/resources/browse/modern-greek-texts-corpus-makedonia-newspaper-annotated-by-the-grne-tagger/76777cae4c8811e89c6caa3fc6ebde2ce44e9fd17cce43d8ab298aae0c7058fe/) link and move the unzipped folder in the same path with the scripts.
* Step 5: `python making_entity_list.py`: Creates the entity list from the dataset.
* Step 6: `python edit_entity_list.py`: Removes insufficient records from the list, entities with less than 4 characters and sort the list by the length of the named entity.
* Step 7: `python parsing_entitites.py`: Extracts the annotated entities from the sentences.
* Step 8: `python convert_to_biluo.py`: Converts the entities to biluo format.
* Step 9: `python convert_to_json_format_and_split_to_train_dev.py`: Uses only the records with proper tokenization and the existence of entities in the sentences, for the creation of train and dev data.

It must be noted that configuration has to be done in the init file of lang/el, so the proper tag_map is used.
The model has been trained using as pretrained vectors the Greek, FastText, Common Crawl vectors from [this](https://fasttext.cc/docs/en/crawl-vectors.html) link. The POS Tagger and the Entity Recognizer are provided from the model.
