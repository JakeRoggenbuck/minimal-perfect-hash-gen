current_arr_size = 10
test = ["hello", "there", "my", "name", "is", "teo", "honda", "scully"]

words = []

with open("wordlist.txt") as file:
    #words = file.readlines()[:current_arr_size]
    pass

def hash_(word, m):
    c = ''.join(format(ord(i),'b').zfill(8) for i in word)
    d = (int(c) * m) >> (len(c) - 4)
    return d % len(test)
    
for m in range(10000):
    d = {}
    for word in test:
        c = hash_(word, m)
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if len(d.keys()) == len(test):
        print(f'{d} | {m}')
