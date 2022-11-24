import threading

current_arr_size = 100
thread_count = 4

words = []

char_to_int = {'a': '0', 'b': '1', 'c': '2', 'd': '3',
'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 
'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13',
'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18',
't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 
'y': '24', 'z': '25', 'I': '26', '\n': 0}

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
    return c % current_arr_size

#sort()

# h(k) = ((ak + b)%p)%m

# Can you judge future parameters on past performance?
best_of_the_best = []
def gen_parameters(word_list, thread_num):
    start = (current_arr_size // thread_count) * (thread_num - 1)
    end = (current_arr_size // thread_count) * (thread_num)
    count = current_arr_size

    for a in range(start, end):
        for b in range(1, current_arr_size):
            frequency: list = [0 for x in range(current_arr_size)]
            for i in words:
                frequency[h_(a, b, i)] += 1
            collisions = len(list(filter(lambda x: not x, frequency)))
            if count > collisions:
                count = collisions
                best = [a, b]
    best_of_the_best.append(best)

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

print(f'a: {get_best(best_of_the_best)[0]} \nb: {get_best(best_of_the_best)[1]}')
    