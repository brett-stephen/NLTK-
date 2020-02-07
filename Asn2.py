# CPSC 4310/5310/7310   Assignment 2
# Q3. [15 points]
# Brett Dziedzic

from nltk.corpus import brown #corpus to test
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE # Class for providing Maximum Likelihood Estimator ngram model scores
#corpus = brown.words()
corpus = brown.sents(categories='news') #Used news corpus instead of entire corpus to cut down on computation time

val = int(input("Choose # of words:\n"))
num_words = val
val = input("Choose variant: \n 'a'  bi-gram model\n 'b' tri-gram model\n")
n = 0

if val == 'a':
    n = 2
else:
    n = 3

train_data, padded_sents = padded_everygram_pipeline(n, corpus)
lang_model = MLE(n) # creates an n-gram language model with specified n
lang_model.fit(train_data, padded_sents) # updates models stats with training data

print(lang_model.generate(num_words, random_seed=0))