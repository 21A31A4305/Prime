def prime(n,c):
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n,end=" ")
    else:
        return
n=int(input())
for j in range(1,n+1):
    c=0
    prime(j,c)
