import string

text = input("Paste text here: ")

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1


for word in freq:
    print(word, freq[word])