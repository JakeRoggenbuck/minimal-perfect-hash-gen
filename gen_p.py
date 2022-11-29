"""
Program to find prime p > biggest c of list size m
c is a unique integer string unique to any alpha string

Teo Honda-Scully | 2022 
"""

char_to_int = char_to_int = {'\n': 0, 'a': 1, 'b': 6, 'c': 19, 'd': 20, 'e': 41, 'f': 165, 'g': 166, 'h': 333, 'i': 667, 'j': 2002, 'k': 2003, 'l': 2004, 'm': 4009, 'n': 8019, 'o': 24058, 'p': 48117, 'q': 48118, 'r': 48119, 's': 144358, 't': 721791, 'u': 2165374, 'v': 4330749, 'w': 4330750, 'x': 4330751, 'y': 4330752, 'z': 8661505, 'I': 8661506}

# q = placeholder for biggest c
q = 0

def c(k) -> int:
    c = 0
    for i in k:
        c += char_to_int[i]
    return c

word_to_c = {}

with open("wordlist.txt") as file:
    for word in file.readlines():
        word_to_c[word] = c(word)

# Sanity check: assert no repeats in word_to_c.values(). If no print, each k has a unique c :)
freq = {}
for c in word_to_c.values():
    if c in freq:
        print(c)

for c in word_to_c.values():
    if c > q:
        q = c

print(q)
# Stuck on a function that finds the next prime number. Will do research later haha