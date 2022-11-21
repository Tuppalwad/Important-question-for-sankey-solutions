def Mearg(l1,m,l2,n):
    x=[]
    if m<0 :
        x=l2[:n]
    elif n<0:
        x=l1[:m]
    else:
        x=l1[:m] + l2[:n] 
        
    x.sort()
    return x 

l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
n=int(input())
print(Mearg(l1,m,l2,n))