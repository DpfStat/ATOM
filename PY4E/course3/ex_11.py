import re
fh = open("11_2.txt")
sum = 0
value = list()
for line in fh:
    line = line.rstrip()
    words = re.findall("[0-9]+", line)
    for word in words:
        v = int(word)
        value.append(v)
        sum = sum + v
print(sum)
