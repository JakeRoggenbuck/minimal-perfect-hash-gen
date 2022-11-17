import random
import math

words = []

with open("wordlist.txt") as file:
    for line in file.readlines():
        words.append(line)

char_to_int = {'a': '0', 'b': '1', 'c': '2', 'd': '3',
'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 
'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13',
'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18',
't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 
'y': '24', 'z': '25', 'I': '26'}

def conv_str_to_int(word):
    word = word.replace("\n", "")
    word_ = ""
    for letter in word:
        word_ += char_to_int[letter]
    return word_

ord_arr = [conv_str_to_int(words[i]) for i in range(len(words))]

def hash(word):
    a = 0
    b = 0
    pass