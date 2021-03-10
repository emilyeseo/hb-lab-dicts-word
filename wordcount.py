def dictionary(openfile):
    lines = open(openfile)

    word_count_list = {}
    for line in lines:
        line = line.rstrip()
        words = line.split()

        for word in words:
            word_count_list[word] = word_count_list.get(word, 0) + 1

    for word, count in word_count_list.items():
        print(word, count)


print(dictionary("test.txt"))
