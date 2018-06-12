import pandas as pd
import numpy as np
import re,string

# load all songs
songs = pd.read_csv('./maroon5-songs.csv')
words = []
sentences = []
# merge all the lyrics together into one huge string
exclude = set(string.punctuation)

lyrics = songs['lyrics'].sample(frac=1)
for index, row in lyrics.iteritems():
    l = str(row).lower()
    l = re.sub("\([^)]*\|\[[^)]*\]", "", l)
    l = re.split("[|\-]",l)
    l = list(filter(None, l))
    for each in l:
        s = ''.join(ch for ch in each if ch not in exclude)
        sentences.append(s + ' .')
        words.extend(s.split(' '))
    sentences.append('--sep--')
#print (sentences)
words = sorted(list(set(words)) +['<unk>'])

vocab1 = open('./data/vocab.en', 'w')
vocab2 = open('./data/vocab.vi', 'w')
for word in words:
  vocab1.write("%s\n" % word)
  vocab2.write("%s\n" % word)
# print(words)
print(sentences)


train = []
test = []
val = []
count = 0
tt = []
for sent in sentences:
    if sent != '--sep--':
        count += 1

    if count <= 200:
        val.append(sent)
    elif count > 200 and count <= 400:
        test.append(sent)
    else:
        train.append(sent)

#write train file
en = open('./data/train.en', 'w')
de = open('./data/train.vi', 'w')
prev = ''
for sent in train:
    if prev == '':
        prev = sent
        continue

    if sent == '--sep--':
        prev = ''
        continue

    en.write("%s\n" % prev)
    de.write("%s\n" % sent)
    prev = sent

#write test file
en = open('./data/test.en', 'w')
de = open('./data/test.vi', 'w')
prev = ''
for sent in test:
    if prev == '':
        prev = sent
        continue

    if sent == '--sep--':
        prev = ''
        continue

    en.write("%s\n" % prev)
    de.write("%s\n" % sent)
    prev = sent

#write val file
en = open('./data/val.en', 'w')
de = open('./data/val.vi', 'w')
prev = ''
for sent in val:
    if prev == '':
        prev = sent
        continue

    if sent == '--sep--':
        prev = ''
        continue

    en.write("%s\n" % prev)
    de.write("%s\n" % sent)
    prev = sent


s = open('./data/sentences.txt', 'w')
for sent in sentences:
    if sent == '--sep--':
        continue
    s.write("%s\n" % sent)
