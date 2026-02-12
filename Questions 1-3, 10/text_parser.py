def preprocessor(words):
    clean_tokens = []
    for word in words.split():
        word = word.lower()
        if ord(word[0]) > 122 or ord(word[0]) < 97:
            word = word[1:]
        if ord(word[-1]) > 122 or ord(word[-1]) < 97:
            word = word[:-1]
        if len(word) > 1:
            clean_tokens.append(word)
    return clean_tokens

def find_lines_containing(filename, keyword):
    matches = []
    keyword = keyword.lower()
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            if keyword in line.lower():
                matches.append((i, line.strip()))

    return matches