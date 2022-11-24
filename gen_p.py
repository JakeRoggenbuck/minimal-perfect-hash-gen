"""
Program to find prime p > biggest c of list size m
c is a unique integer string unique to any alpha string

Teo Honda-Scully | 2022 
"""

from math import floor, sqrt

char_to_int = {'\n': 0, 'a': 1, 'b': 6, 'c': 25, 'd': 101, 'e': 405, 
'f': 2836, 'g': 11345, 'h': 45381, 'i': 136144, 'j': 953009, 
'k': 1906019, 'l': 7624077, 'm': 38120386, 'n': 152481545, 
'o': 762407726, 'p': 3812038631, 'q': 15248154525, 'r': 30496309051, 
's': 121985236205, 't': 975881889641, 'u': 4879409448206, 
'v': 19517637792825, 'w': 58552913378476, 'x': 175658740135429, 
'y': 351317480270859, 'z': 1053952440812578, 'I': 4215809763250313}

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
print("...")

for c in word_to_c.values():
    if c > q:
        q = c

# Adjusted from https://www.geeksforgeeks.org/nearest-prime-less-given-number-n/
def nearest_prime(n):
    if (n & 1):
        n -= 2
    else:
        n -= 1
    i,j = 0,3
    for i in range(n, 2, -2):
        if(i % 2 == 0):
            continue
        while(j <= floor(sqrt(i)) + 1):
            if (i % j == 0):
                break
            j += 2
        if (j > floor(sqrt(i))):
            return i
    return 2

print("Please wait...")
print(nearest_prime(q))

    