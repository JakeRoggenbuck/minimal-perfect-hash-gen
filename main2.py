with open("wordlist.txt") as file:
    for line in file.readlines():
        #words.append(line)

def gen_parameters(word_list):
    a = 0
    b = 0
    pass

["hello", "hi", "rpoeajkrpoejkorjeporj", "bye"]
len(list) = 4

hash table -> array, index == hash(key), element = key
1.3 * key = size of array

key amount = size of array
1 * key = size of array

hash(key) -> unique index with no collision.  # 1 to 1
                    ^ dependent on hash function AND the set of data

def hash(k): return (((a*k + b) % p) % m)

def gen_parameters(word_list):
    return a, b

k is in [data set]
use_hash(a, b, k):
    return (((a*k + b) % p) % m)