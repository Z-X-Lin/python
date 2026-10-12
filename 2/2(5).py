m=list(map(int,input().split()))
n=len(m)
for i in range(n):
    for j in range(n-1-i):
        x,y=m[j],m[j+1]
        if abs(x)>abs(y) or (abs(x)==abs(y)and x>y):
            m[j],m[j+1]=m[j+1],m[j]
print(m)