name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From"):
        words = line.split()
        if len(words) < 3:
            counts[words[1]] = counts.get(words[1],0)+1
bigemail = None
bigcount = None
for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigemail = email
        bigcount = count
print(bigemail, bigcount)
