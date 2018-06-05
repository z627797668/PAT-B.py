n=input()
n=int(n)
sum=list(range(0,n))
for i in sum:
    str=input()
    nump=0
    numt=0
    la=0
    ma=0
    ra=0
    strlen=len(str)
    t=True
    sumlen=list(range(0,strlen))
    for j in sumlen:
        if(str[j]=='A' or str[j]=='T' or str[j]=='P'):
            if(str[j]=='A' and nump==0 and numt==0):
                la+=1
            elif(str[j]=='A' and nump==1 and numt==0):
                ma+=1
            elif(str[j]=='A' and nump==1 and numt==1):
                ra+=1
            elif(str[j]=='P' and nump!=1):
                nump+=1
            elif(str[j]=='T' and numt!=1):
                numt+=1
            else:
                t=False
                break
        else:
            t=False
            break
    if(t==False):
        print("NO")
    else:
        if(ma!=0 and ra==(ma*la) and nump==1 and numt==1):
            print("YES")
        else:
            print("NO")
