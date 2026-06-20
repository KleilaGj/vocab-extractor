import string

text = input("Paste text here: ")

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

print(words)