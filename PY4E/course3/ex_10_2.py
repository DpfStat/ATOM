name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        num = line.find(":")
# find the mistake about num
#        print(line, num)
        # if num > 4:
        counts[line[num-2:num]] = counts.get(line[num-2:num],0)+1
lst = list()
for key, value in counts.items():
    newtemp = (key, value)
    lst.append(newtemp)
lst = sorted(lst)

for key, value in lst:
    print(key, value)
