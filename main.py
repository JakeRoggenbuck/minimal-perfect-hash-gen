import threading

current_arr_size = 200
thread_count = 4
p = 39121129 # from gen_p.py

words = []

char_to_int = {'\n': 0, 'a': 1, 'b': 6, 'c': 19, 'd': 20, 'e': 41, 'f': 165, 'g': 166, 'h': 333, 'i': 667, 'j': 2002, 'k': 2003, 'l': 2004, 'm': 4009, 'n': 8019, 'o': 24058, 'p': 48117, 'q': 48118, 'r': 48119, 's': 144358, 't': 721791, 'u': 2165374, 'v': 4330749, 'w': 4330750, 'x': 4330751, 'y': 4330752, 'z': 8661505, 'I': 8661506}

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]

def h(a, b, k) -> int:
    c = 0
    for i in k:
        c += char_to_int[i]
    q = (a * c // b) % p
    return q % current_arr_size

# h(k) = ((ak + b)%p)%m

# Can you judge future parameters on past performance?
best_of_the_best = []
coll = [] # SCUFFED but it is fine.
def gen_parameters(word_list, thread_num):
    start = (current_arr_size // thread_count) * (thread_num - 1)
    end = (current_arr_size // thread_count) * (thread_num)
    count = current_arr_size

    for a in range(start, end):
        for b in range(1, current_arr_size):
            frequency: list = [0 for x in range(current_arr_size)]
            for i in word_list:
                frequency[h(a, b, i)] += 1
            collisions = len(list(filter(lambda x: not x, frequency)))
            if count > collisions:
                count = collisions
                best = [a, b]
    best_of_the_best.append(best)
    coll.append(count)

threads = []
for x in range(thread_count): 
    t = threading.Thread(target=gen_parameters, args=(words, x + 1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(best_of_the_best)

def get_best(bests):
    best_list = []
    best_count = 10000000
    for i in bests:
        count = 0
        count += (i[0] + i[1])
        if count < best_count:
            best_count = count
            best_list = i
    return best_list

print(f'a: {get_best(best_of_the_best)[0]} \nb: {get_best(best_of_the_best)[1]} \ncoll: {coll[0]}')
 