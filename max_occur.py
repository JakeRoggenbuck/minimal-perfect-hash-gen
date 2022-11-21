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
        

print(letter_max_occurrence)