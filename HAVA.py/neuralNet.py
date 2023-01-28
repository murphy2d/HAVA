import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

#making neurons for AI

Stemmer = PorterStemmer()

def tokenize(sentence):                #ALl data is received by brain and then processed
                                       #tokenize means to split like 'hello' to 'h,e,l,l,o' . 
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())  #does a formality, converts into words

def bag_of_words(tokenized_sentence, words):
    sentence_word = [stem(word) for word in tokenized_sentence]   #this packs the words into a bag
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1

    return bag