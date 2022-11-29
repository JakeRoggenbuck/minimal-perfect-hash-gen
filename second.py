current_arr_size = 15

words = []

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]

def hash_(word, m):
    c = ''.join(format(ord(i),'b').zfill(8) for i in word)
    d = (int(c) * m) >> (len(c) - 4)
    return d % len(words)
    
for m in range(30000):
    d = {}
    for word in words:
        c = hash_(word, m)
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if len(d.keys()) == len(words):
        print(f'{d} | {m}')
