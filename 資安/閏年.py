y=int(input())
m=int(input())
d=int(input())

m1=0
m2=0
m3=0

if y%4 == 0:
    if y%100 == 0:
        if y%400 ==0:
            n=1
        else:
            n=0    
    else:
        n=1
else:
    n=0

if m%2 == 0 :
    m2= (m-1)//2*(30+31)+31-2
else:
    if m == 1:
        m3=0
    else:   
        m1= (m-1)//2*(30+31)-2

ans=m1+m2+m3+n+d
print(ans)
    
    

    