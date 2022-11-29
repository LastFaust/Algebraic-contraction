import os
global write_bit
global bit_len

with open("output.txt", "rb") as file:
    text = ord(file.read(1))
    print(text)
    dictionary = {}
    for i in range(text):
        key_word = file.read(1).decode('ascii')
        # print(key_word)
