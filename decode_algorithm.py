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
    # алгоритм раскодирования
    with open("output.txt", "wb+") as output_file:
        low_interval = 0
        high_interval = (1 << 16) - 1
        delete = work_interval[-1]
        diff = high_interval - low_interval + 1
        first_q = int(int(high_interval + 1) / 4)
        half_q = first_q * 2
        third_q = first_q * 3
        val = 0
        
