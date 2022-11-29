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
    with open("output.txt", "wb+") as output_file:
        low_interval = 0
        high_interval = (1 << 16) - 1
        delete = work_interval[-1]
        diff = high_interval - low_interval + 1
        first_q = int(int(high_interval + 1) / 4)
        half_q = first_q * 2
        third_q = first_q * 3
        val = 0

        for iterator in range(16):
            k = in_put_bit(output_file)
            val += val + k
        while True:
            fraq = int((val - low_interval + 1) * delete - 1) / diff
            j = 1
            while work_interval[j] <= fraq:
                j += 1
            high_interval = int(low_interval + work_interval[j] * diff / delete - 1)
            low_interval = int(low_interval + work_interval[j-1] * diff / delete)

            while True:
                if high_interval < half_q:
                    pass
                elif low_interval >= half_q:
                    low_interval -= half_q
                    high_interval -= half_q
                    val -= half_q
                elif low_interval >= first_q and high_interval < third_q:
                    low_interval -= first_q
                    high_interval -= first_q
                    val -= first_q
                else:
                    break
                output_file.write(list(dictionary.keys())[j-2].encode('ascii'))
                diff = high_interval - low_interval + 1
output_file.close()
