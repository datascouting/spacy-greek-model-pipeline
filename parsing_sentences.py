# -*- coding: utf-8 -*-
import codecs
from lxml import etree
import json

names = {
    'types': "http:///gr/ilsp/types.ecore",
    'xmi': "http://www.omg.org/XMI"
}

n = {
    'cas': "http:///uima/cas.ecore",
    'xmi': "http://www.omg.org/XMI"
}

for i in range(1696):
    file = './755b062e73e111e5b5c6aa3fc8d33ad892be00b397914b38a887df7ee45fb3f9/archive/split' + \
        str(i)+'_makedonia.txt'

    print(file)

    article = etree.parse(file)

    with codecs.open('sentences.json', 'w', encoding='utf-8', errors='ignore') as sentences, \
            codecs.open(file, 'r', encoding='utf-8', errors='ignore') as file:
        sofas = article.xpath(
            "cas:Sofa/@sofaString",
            namespaces=n
        )[0]  # news text

        begin_tokens = article.xpath("//types:Token/@begin", namespaces=names)
        end_tokens = article.xpath("//types:Token/@end", namespaces=names)

        # index of token in sentence
        sent_ord = article.xpath("//types:Token/@sentOrd", namespaces=names)
        num_sentences = len(article.xpath(
            "//types:Sentence/@end",
            namespaces=names
        ))

        # pos id to locate the class
        pos_tokens_id = article.xpath(
            "//types:Token/@posTag",
            namespaces=names
        )

        index = 0

        for num in range(num_sentences):
            sentence = ''

            while 1:
                begin_token_index = int(begin_tokens[index])
                end_token_index = int(end_tokens[index])
                token_value = sofas[begin_token_index:end_token_index]
                sentence = sentence + token_value + ' '
                index = index + 1

                if len(sent_ord) == index or sent_ord[index] == '1':
                    if sentence[:-1] != '* * * * * * * * * * * * * *':  # ignore noise
                        my_dict = {"sentence": u''.join(sentence[:-1])}
                        json.dump(my_dict, sentences, ensure_ascii=False)
                        sentences.write('\n')

                    break
