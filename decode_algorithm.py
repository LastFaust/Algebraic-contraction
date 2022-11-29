import os

global read_bit
global bit_len
global rubbish_bit
rubbish_bit = 0
bit_len = 0
read_bit = 0

def in_put_bit(file):
    global read_bit
    global bit_len
    global rubbish_bit
    if (bit_len == 0):
        bit = file.read(1)
        read_bit = int.from_bytes(bit, "little")
         if (bit == b""):
            rubbish_bit += 1
            read_bit = 255
            if (rubbish_bit > 14):
                exit(1)
        bit_len = 8
    t = read_bit & 1
    read_bit >>= 1
    bit_len -= 1
    return t

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
        
