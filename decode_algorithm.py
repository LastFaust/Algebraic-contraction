import os
global write_bit
global bit_len

with open("coded_text.txt", "rb") as coded_text_file:
    text = ord(coded_text_file.read(1))
    print(text)
    dictionary = {}
    for i in range(text):
        key_hadder = coded_text_file.read(1).decode('ascii')
        # print(key_word)
        value_hadder = int.from_bytes(coded_text_file.read(4), "little")
        dictionary[key_hadder] = value_hadder
    # print(dictionary)

    work_interval = [0, 1]
    for i in dictionary:
        work_interval.append(dictionary[i] + work_interval[-1])
    # print(work_interval)

    # алгоритм раскодирования
    with open("output.txt", "wb+") as output_file:
        
