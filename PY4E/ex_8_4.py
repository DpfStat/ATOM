fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Wrong input")
    quit()
lst = list()
for line in fh:
    newline = line.rstrip()
    words = newline.split()
    for word in words:
        if word in lst:
            continue
        lst.append(word)
lst.sort()
print(lst) 
