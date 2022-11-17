words = []

with open("wordlist.txt") as file:
    for line in file.readlines():
        words.append(line)

print(words)