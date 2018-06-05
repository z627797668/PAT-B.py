n=input()
n=int(n)
sum=list(range(0,n))
i=0
minname=''
minid=''
maxname=''
maxid=''
maxgrade=-1
mingrade=101
for i in sum:
    name,id,grade=input().split()
    grade=int(grade)
    if(maxgrade<grade):
        maxname=name
        maxid=id
        maxgrade=grade
    if(mingrade>grade):
        minname=name
        minid=id
        mingrade=grade
print(maxname+" "+maxid)
print(minname+" "+minid)
