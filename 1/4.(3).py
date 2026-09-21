import math
a=float(input())
b=float(input())
c=float(input())
if a+b>c and a+c>b and b+c>a:
    p=float((a+b+c)/2)
C=float(p*2)
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(C,s)