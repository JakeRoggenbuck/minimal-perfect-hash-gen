current_arr_size = 100

words = []
frequency: list = [0 for x in range(current_arr_size)]

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]

def gen_parameters(word_list):
    a = 1
    b = 1
    return a, b

a, b = gen_parameters(words)

def djb2(a, b, raw) -> int:
    h = a
    for c in raw:
        h = ((h << b) + h) + ord(c)
    return int(h) % current_arr_size

for i in words:
    frequency[djb2(a, b, i)] += 1

collisions = len(list(filter(lambda x: not x, frequency)))
print(collisions)
print(frequency)

# Can you judge future parameters on past performance?