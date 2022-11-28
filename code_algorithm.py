import os

dictionary_sum = 0
with open('in.txt', 'r') as fp:
    text_sum = 0
    text = fp.read(1)
    dictionary = {}
    while text:
        text_sum += 1
        if dictionary.get(text) == None:
            dictionary.update({text: 1})
        else:
            dictionary[text] = dictionary[text] + 1

        text = fp.read(1)
        # print(text)
    # print(dictionary)

    for val in dictionary.items():
        dictionary_sum = dictionary_sum + val
    if text_sum == dictionary_sum:
        print("Ok")
    else:
        print("Couldn't write to file")
        exit()

dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
# print(dictionary)

work_interval = [0, 1]
for i in dictionary:
    work_interval.append(dictionary[i] + work_interval[-1])

f = open("output.txt", "wb+")
print(len(dictionary))
f.write(len(dictionary).to_bytes(1, "little"))
for i in dictionary:
    f.write(i.encode("ascii"))
    f.write(dictionary[i].to_bytes(4, "little"))
print(dictionary)
