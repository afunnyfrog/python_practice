y=int(input())
m=int(input())
d=int(input())

m1=0
m2=0
m3=0
m4=0
    
if y%400 == 0:
    n=1
elif y%100 == 0 :
    n = 0
elif y%4== 0:
    n=1
else:
    n=0

if m == 2 :
    m1= 31
elif m == 1:
    m2=0
elif m%2 == 0:
    m3=(m-1)//2*(30+31)-2+31
elif m%2 == 1:
    m4=(m-1)//2*(30+31)-2
elif 1 >= m >=12:
    print("有效的月份")
else:   
    print("無效的月份")

ans=m1+m2+m3+m4+n+d
print(ans)
    
    

    