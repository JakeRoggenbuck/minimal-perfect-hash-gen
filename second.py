current_arr_size = 10
test = ["hello", "there", "my", "name", "is", "teo", "honda", "scully"]

words = []

with open("wordlist.txt") as file:
    #words = file.readlines()[:current_arr_size]
    pass

m = 31
def hash(word):
    c = ''.join(format(ord(i),'b').zfill(8) for i in word)
    d = (int(c) * m) >> (len(c) - 4)
    return d % len(test)
    
for word in test:
    print(hash(word))
    for m in range(10000):
        