n=input()
n=int(n)
a=list(range(0,n//100))
b=list(range(0,n//10%10))
c=list(range(0,n%10))
for i in a:
    print("B",end="")
for i in b:
    print("S",end="")
for i in c:
    print(i+1,end="")
