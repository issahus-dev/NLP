import spacy

nlp = spacy.load('en_core_web_md')

nlps = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana')
tokens2 = nlp('car driver phone apple')
#s stands for simple
tokens_s = nlps('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

for token1 in tokens2:
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

"""what i found interesting was the fact the system was able to identify a strong similarity between a banana and a monkey,
however not a strong similarity between a apple and a monkey"""

for token1 in tokens_s:
    for token2 in tokens_s:
        print(token1.text, token2.text, token1.similarity(token2))

"""the difference that i found was that the larger language model was more accurate, for instances with the smaller language model
it found a larger similarity between a cat and a apple than a cat and a monkey.
"""
