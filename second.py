current_arr_size = 200

words = []

with open("wordlist.txt") as file:
    words = file.readlines()[:current_arr_size]