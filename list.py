fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
            lst.sort()
    # print(len(words))
    # print(lst.append(words))
    # list = lst.append(words)
    # word = num.sort()


print(lst)