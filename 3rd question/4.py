# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 22:06:59 2019

@author: LENOVO
"""

import re
names = []
n = int(input())
for x in range(n):
    input_text = str(input())
    names.append(input_text)
#print(names)
with open('corpus.txt','r',encoding='utf8') as corpus:
    lines = corpus.read().splitlines()
answers = []
def gender():
    for i in range(len(names)):
        name = names[i]
        male = 0
        female = 0
        name_docs = []
        tokens = []
        name_docs = [line for line in lines if name in line]
        for doc in name_docs:
            tokens = re.split('\s',doc)
            if 'he' in tokens or 'his' in tokens or 'him' in tokens:
                male += 1
            if 'she' in tokens or 'her' in tokens or 'hers' in tokens:
                female += 1

        if male>female:
            answers.append('Male')
        else:
            answers.append('Female')

    return answers



print(gender())