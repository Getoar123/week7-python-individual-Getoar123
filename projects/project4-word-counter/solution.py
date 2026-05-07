# Project 4 — Word Counter
# Author: Getoar Sopa

sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Total words
total_words = len(words)

# Total characters (remove spaces)
total_chars = len(sentence.replace(" ", ""))

# Word frequency dictionary
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print results
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print("Word frequency:")

for word, count in frequency.items():
    print(f"  {word} -> {count}")
