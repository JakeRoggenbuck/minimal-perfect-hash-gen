import threading

current_arr_size = 2000
thread_count = 4
p = 421693816493 # from gen_p.py

words = []

char_to_int = {'\n': 0, 'a': 1, 'b': 6, 'c': 25, 'd': 101, 'e': 405, 
'f': 2836, 'g': 11345, 'h': 45381, 'i': 136144, 'j': 953009, 
'k': 1906019, 'l': 7624077, 'm': 38120386, 'n': 152481545, 
'o': 762407726, 'p': 3812038631, 'q': 15248154525, 'r': 30496309051, 
's': 121985236205, 't': 975881889641, 'u': 4879409448206, 
'v': 19517637792825, 'w': 58552913378476, 'x': 175658740135429, 
'y': 351317480270859, 'z': 1053952440812578, 'I': 4215809763250313}

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]

def h_(a, b, raw) -> int:
    h = a
    for c in raw:
        h = ((h << b) + h) + ord(c)
    return int(h) % current_arr_size

def h2(a, b, raw) -> int:
    c = '0'
    for i in raw:
        c += char_to_int[i] + a
        c %= b
        print(type(a))
    return c % current_arr_size

def h3(a, b, k) -> int:
    c = 0
    for i in k:
        c += char_to_int[i]
    q = (a * c + b) % p
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
                frequency[h3(a, b, i)] += 1
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
 