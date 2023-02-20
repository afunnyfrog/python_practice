money=int(input())

a=1000000
b=2000000
c=4000000
d=6000000
e=10000000

A=a*0.1
B=(b-a)*0.07
C=(c-b)*0.05
D=(d-c)*0.04
E=(e-d)*0.02

if money <= a:
    get = round(A)
else:
    if money <= b:
        get = round(A+(money-a)*0.07)
    else:
        if money <= c:
            get= round(A+B+(money-b)*0.05)
        else:
            if money <= d:
                get= round(A+B+C+(money-c)*0.04)
            else:
                if money <= e:
                    get= round(A+B+C+D+(money-d)*0.02)
                else:
                    if money >= e:
                        get= round(A+B+C+D+E+(money-e)*0.01)

print(get)
        