str=input()
count=0
s=[temp for temp in str.split(" ")]
lenlist=len(s)-1
while lenlist>=0:
    if lenlist!=0:
        print(s[lenlist],end=" ")
    else:
        print(s[lenlist],end="")
    lenlist-=1
