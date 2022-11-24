"""
Program to find prime p > biggest c of list size m
c is a unique integer string unique to any alpha string

Teo Honda-Scully | 2022 
"""

char_to_int = {'\n': 0, 'a': 1, 'b': 6, 'c': 25, 'd': 101, 'e': 405, 
'f': 2836, 'g': 11345, 'h': 45381, 'i': 136144, 'j': 953009, 
'k': 1906019, 'l': 7624077, 'm': 38120386, 'n': 152481545, 
'o': 762407726, 'p': 3812038631, 'q': 15248154525, 'r': 30496309051, 
's': 121985236205, 't': 975881889641, 'u': 4879409448206, 
'v': 19517637792825, 'w': 58552913378476, 'x': 175658740135429, 
'y': 351317480270859, 'z': 1053952440812578, 'I': 4215809763250313}

def h3(a, b, k) -> int:
    c = '0'
    for i in k:
        c += char_to_int[i]
    q = (a * c + b) % p
    return q % current_arr_size

# h(k) = ((ak + b)%p)%m
