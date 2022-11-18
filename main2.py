current_arr_size = 200

words = []
map = {} 

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]

def h_(a, b, raw) -> int:
    h = a
    for c in raw:
        h = ((h << b) + h) + ord(c)
    return int(h) % current_arr_size

count = current_arr_size
best: list
for a in range(current_arr_size):
    for b in range(current_arr_size):
        frequency: list = [0 for x in range(current_arr_size)]
        for i in words:
            frequency[h_(a, b, i)] += 1
        collisions = len(list(filter(lambda x: not x, frequency)))

        if count > collisions:
            count = collisions
            best = [a, b]

# Can you judge future parameters on past performance?
print(f"best combo: {best:} \ncollisions: {count:}\nlist size: {current_arr_size:}")

def gen_parameters(word_list):
    a = 1
    b = 1
    return a, b