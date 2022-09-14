import random as rd
import json as js
import csv
import re

import string


txt = open("/Users/guillaumepaviot/Documents/Projects/Markov_Chain/Text.rtf", "r")
txt = txt.read()
txt = txt.lower()



order = 5
ngram = {}

for i in range(len(txt)-order):

    gram = txt[i:i+order]

    if gram not in ngram:
        ngram[gram] = []

    ngram[gram].append(txt[i+order])

def markovIt():

    currentGram = "enfer"
    result = currentGram

    for i in range(400):
        possibilities = ngram[currentGram]
        next = rd.choice(possibilities)
        result += str(next)
        currentGram = result[i+1:i+9]

    print(result)


markovIt()
