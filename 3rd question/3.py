# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:04:25 2019

@author: LENOVO
"""

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

n = int(input())

allparts = []
for i in range(n):
    allparts.append(input())
input()  # *****
for i in range(n):
    allparts.append(input())

# Loop over all possible pairs, selecting in order of max value

tfidf = TfidfVectorizer(stop_words='english').fit_transform(allparts)
pairwise_similarity = cosine_similarity(tfidf, tfidf)

crosscorr = pairwise_similarity[n:, :n]
pairvals = [0] * n
for i in range(n):
    idx = np.argmax(crosscorr, axis=None)
    print(idx)
    multi_idx = np.unravel_index(idx, crosscorr.shape)
    pairvals[multi_idx[0]] = multi_idx[1]
    crosscorr[multi_idx[0], :] = np.ones(n) * -1
    crosscorr[:, multi_idx[1]] = np.ones(n) * -1
    
for v in pairvals:
    print(v+1)