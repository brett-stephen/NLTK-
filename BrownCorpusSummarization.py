#import nltk
#nltk.download()
#https://www.youtube.com/watch?v=FLZvOKSCkxY

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown

totalTokens = 0
example_test = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pink, and you should not go outside."

val = input("Choose variant: \n 'a'  with stopwords, \n 'b'  without stopwords, \n 'c' without stopwords and lemmatization,\n 'd' without stopwords and stemming.")

if val == 'a':
  print("b is greater than a")
elif val == 'b':
  print("a and b are equal")
elif val == 'c':
  print("a and b are equal")
elif val == 'd':
  print("a and b are equal")


for m in brown.categories():
        print(m)
        categoryTokens = len(brown.words(categories=m))
        print(f'    Total Tokens: {categoryTokens}')
        print(f'    Total Types: {len(set(brown.words(categories=m)))}')
        totalTokens = categoryTokens + totalTokens

print(f'Total Tokens of whole corpus: {totalTokens} Tokens ')

print(sent_tokenize(example_test))
print(word_tokenize(example_test))
print(len(example_test))