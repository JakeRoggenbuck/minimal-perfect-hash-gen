"""
Returns a key-value map of data of each letter's max occurrence in a single word per file
Teo Honda-Scully | 2022. 
Pairs with main3.py
"""

words = []
letter_max_occurrence = {}
current_arr_size = 600

alpha = "abcdefghijklmnopqrstuvwxyzI"
for letter in alpha:
    letter_max_occurrence[letter] = 0

with open("wordlist.txt") as file:
    for word in file.readlines()[:current_arr_size]:
        local_letter_occurrence = {}
        for letter in word.rstrip():
            if letter in local_letter_occurrence:
                local_letter_occurrence[letter] += 1
            else:
                local_letter_occurrence[letter] = 1
            for letter in letter_max_occurrence:
                if local_letter_occurrence.get(letter, 0) > letter_max_occurrence[letter]:
                    letter_max_occurrence[letter] = local_letter_occurrence[letter]

# Prints the raw max letter occurrence (ex. 7 e's means 1 word in wordlist.txt contains 7 e's)
print(str(letter_max_occurrence) + "\n")

char_to_int = {'a' : 1}
for key in letter_max_occurrence:
    if key == 'a':
        continue
    char_to_int[key] = char_to_int[alpha[alpha.index(key) - 1]] * letter_max_occurrence[alpha[alpha.index(key) - 1]] + 1
print(char_to_int)

def get_char_to_int():
    return char_to_int

def get_arr_size():
    return current_arr_size