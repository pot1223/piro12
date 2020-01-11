N=int(input())
n=0

def a(b):
    c=list(map(int,str(b)))
    a=b+sum(c)

    return a
while a(n)!=N:
    if n ==N:
        n=0
        break
    else:
     n+=1

print(n)