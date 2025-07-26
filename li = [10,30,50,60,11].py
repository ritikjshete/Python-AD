li = [10,30,50,60,11]
num = int(input("enter the heighst no you like to find :"))
n = len(li)

for i in range(n):
    for j in range(0,n-i-1) :
       if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li[n-num])
