str=input()
sum=0
i=0
num=[]
ansstr=["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]
for ch in str:
    sum+=int(ch)
if sum==0:
    print("ling")
else:
    while sum>0:
        num.append(int(sum%10))
        i+=1
        sum=sum//10   #python除法
    i-=1
    while i>=0: 
        if i!=0:
            print(ansstr[num[i]],end=' ')
        else:
            print(ansstr[num[i]])
        i-=1
