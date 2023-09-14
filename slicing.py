fhand = open("mbox-short.txt.txt")
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    colpos = line.find(":")
    numbers = float(line[colpos+1:])
    total = total + numbers
    count = count + 1
average = total / count
print("Average spam confidence: ", average)
    # print(line)
    # print(len(line))


