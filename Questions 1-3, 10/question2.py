from text_parser import preprocessor
from collections import Counter

clean_tokens = []
with open('sample-file.txt','r') as f:
    words = f.read()
    clean_tokens = preprocessor(words)

bigram_frequency = {}
for i in range(len(clean_tokens)-1):
    bigram = clean_tokens[i]+clean_tokens[i+1]
    if bigram not in bigram_frequency:
        bigram_frequency[bigram] = 1
    else:
        bigram_frequency[bigram] += 1

ten_most_frequent_bigrams = Counter(bigram_frequency).most_common(10)
print(ten_most_frequent_bigrams)
