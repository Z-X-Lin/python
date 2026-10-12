a=list(map(int,input().split('，')))
b=list(map(int,input().split('，')))
c=a+b
c.sort(reverse=True)
print(c)