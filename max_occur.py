"""
Returns a key-value map of data of each letter's max occurrence in a single word per file
Teo Honda-Scully | 2022. 

Pairs with main3.py
"""

words = []
letter_max_occurrence = {}

alpha = "abcdefghijklmnopqrstuvwxyz"
for letter in alpha:
    letter_max_occurrence[letter] = 0

with open("wordlist.txt") as file:
    for word in file.readlines():
        local_letter_occurrence = {}
        for letter in word.rstrip():
            if letter in local_letter_occurrence:
                local_letter_occurrence[letter] += 1
            else:
                local_letter_occurrence[letter] = 1
            for letter in letter_max_occurrence:
                if local_letter_occurrence.get(letter, 0) > letter_max_occurrence[letter]:
                    letter_max_occurrence[letter] = local_letter_occurrence[letter]

print(letter_max_occurrence)