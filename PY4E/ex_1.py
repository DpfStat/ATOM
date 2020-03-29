# # 5.1
# hrs = input("Enter Hours:")
# h = float(hrs)
# if h <= 40:
#     pay=h*10.5
# else:
#     pay=h*10.5+(h-40)*0.5*10.5
# print(pay)

#5.2
# score = input("Enter Score: ")
# s = float(score)
# if s>1 or s<0:
#     print('error')
# elif s >=0.9:
#     print("A")
# elif s>=0.8:
#     print("B")
# elif s>=0.7:
#     print("C")
# elif s>=0.6:
#     print("D")
# elif s<0.6:
#     print("F")

# # 6
# def computepay(h,r):
#     if h <= 40:
#          return h*r
#     else:
#          return h*r+(h-40)*0.5*r
#
#
# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")
# h = float(hrs)
# r = float(rate)
# p = computepay(h,r)
# print("Pay",p)

# 7
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
# try and except to catch the wrong input
    try :
        fval = int(num)
    except:
        print("Invalid input")
        continue
    print(fval)
# give value to largest and smallest
    if largest is None:
        largest = fval
    if smallest is None:
        smallest = fval
#  iteration
    if largest < fval:
        largest = fval


    if smallest > fval:
        smallest = fval


print("Maximum is", largest)
print("Minimum is", smallest)
