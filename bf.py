#step1 Get data in raw html and convert it to text file

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import unicodedata
from tqdm import tqdm
import os
import pandas as pd


text=open("datasetwa.txt",'r')
soup = BeautifulSoup(text)
text = soup.get_text()
text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')

os.chdir("/Users/nishantsethi/Desktop/arbunize/word2vec");  #directory
df = pd.read_csv('intersect_uni_bigram.csv');
z=df['b'].values.tolist()


#print (text)
#print(type(text))

text = text.lower()
text=text.replace("/", " ")
text=text.replace("&","")
text=text.replace(","," ")
"""text=text.replace("machine learning","machine-learning")
text=text.replace("artificial intelligence", "artificial-intelligence")
text=text.replace("adobe illustrator","adobe-illustrator")
text=text.replace("adobe photoshop","adobe-photoshop")"""


for item in tqdm(z):
    if len(item.split())==2:
        bi = item.split()
        text=text.replace(item,str(bi[0] + "-" + bi[1]))
        print(bi)
        print(bi[0])

text=text.split()
print(type(text))
filtered_text=[w for w in text if w not in (stopwords.words('english'))]

filtered_text = " ".join(filtered_text)

#print(filtered_text)

with open("Outputslash.txt", "w") as text_file:
    text_file.write(filtered_text)

#word_tokens = word_tokenize(text)
#filtered_sentence = [w for w in word_tokens if not w in stop_words]
#filtered_sentence = []
#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)
#print(word_tokens)
#print(filtered_sentence)
#print(len(filtered_sentence))
#sent_text = nltk.sent_tokenize(text)
#for sentence in sent_text:
    #tokenized_text = nltk.word_tokenize(sentence)
    #tagged = nltk.pos_tag(tokenized_text)
    #print(tagged)
