import os

dictionary_sum = 0
with open('in.txt', 'r') as f:
    text_sum = 0
    text = f.read(1)
    dictionary = {}
    while text:
        text_sum += 1
        if dictionary.get(text) == None:
            dictionary.update({text: 1})
        else:
            dictionary[text] = dictionary[text] + 1

        text = f.read(1)
        # print(text)
    # print(dictionary)

    for val in dictionary.items():
        dictionary_sum = dictionary_sum + val
    if text_sum == dictionary_sum:
        print("File read successfully")
    else:
        print("Couldn't write to file")
        exit()
