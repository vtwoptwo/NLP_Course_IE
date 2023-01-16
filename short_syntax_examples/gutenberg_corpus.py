import nltk 
from nltk.corpus import gutenberg

# electronic text archive which contains some 25,000 free electroic books

nltk.corpus.gutenberg.fileids()
# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', '

emma_w = nltk.corpus.gutenberg.words('austen-emma.txt') # use the words() method to tokenize the text
#count the number of words in the text
# using word_tokenize() method
emma_wt = nltk.text.gutenberg.word_tokenize('austen-emma.txt')


len(emma_w)
# 192427

len(emma_wt)
# 192427

#count the average word length in the text
for fileid in gutenberg.fileids(): 
    num_chars = len(gutenberg.raw(fileid)) 
    num_words = len(gutenberg.words(fileid)) 
    num_sents = len(gutenberg.sents(fileid)) 
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)])) 
    print (round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

# MACBETH

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences 
macbeth_sentences[1116]
# get the longest sentence in the text
longest_len = max([len(s) for s in macbeth_sentences])
#the the words in the longest sentence
[s for s in macbeth_sentences if len(s) == longest_len]

