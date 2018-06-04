n=input()
ans=0
n=int(n)
while n!=1:
    ans+=1
    if n%2==0:
        n/=2
    else:
        n=(3*n+1)/2
print(ans)
