# # 7.1
# # Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     line = line.rstrip()
#     line = line.upper()
#     print(line)


# 7.2
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    quit()
n = 0
a = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    ps = line.find(": ")
    value = float(line[ps+2:ps+8])
    a = a + value
    n = n+1

print("Average spam confidence:", float(a/n))
