from text_parser import preprocessor
from collections import Counter

clean_tokens = []
with open('sample-file.txt','r') as f:
    words = f.read()
    clean_tokens = preprocessor(words)
word_frequency_count = {}
for token in clean_tokens:
    if token not in word_frequency_count:
        word_frequency_count[token] = 1
    else:
        word_frequency_count[token] += 1

ten_most_frequent_tokens = Counter(word_frequency_count).most_common(10)
print(ten_most_frequent_tokens)