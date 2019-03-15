#Main file trains data and outputs in a pickle
#Outputwa is with android,web,software,data and Outputwasdg.txt is with all other + graphic
import os
import pandas as pd
import nltk
import gensim
from gensim import corpora ,models, similarities
import pickle
from nltk import bigrams


os.chdir("/Users/nishantsethi/Desktop/arbunize/word2vec");  #directory
file_content = open("Outputslash.txt").read()
sents = nltk.sent_tokenize(file_content)
tokens = []
for sent in sents:
    tokens.append(nltk.word_tokenize(sent))

model = gensim.models.Word2Vec(tokens, min_count=10, size=50, iter=1000)
xd = raw_input("Enter a word")

print(model[xd])
print(model.most_similar(xd))

with open("wordvecpickleslash.pickle", 'wb') as handle:
    pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)
file.close()
