n=input()
sum=list(range(0,int(n)))
hashtable={}
num=[]
num=input().split()
for i in sum:
    num[i]=int(num[i])
hashsum=list(range(0,8888))
for i in hashsum:
    hashtable[i]=0
for i in sum:
    temp=num[i]
    while temp!=1:
        if(temp%2==0):
            temp/=2
            hashtable[temp]=1
        else:
            temp=(temp*3+1)/2
            hashtable[temp]=1
num.sort(reverse=True)
count=0
for i in sum:
    if(hashtable[num[i]]==0):
        count+=1
for i in sum:
    if(hashtable[num[i]]==0):
        count-=1
        if(count!=0):
            print(num[i],end=' ')
        else:
            print(num[i])

