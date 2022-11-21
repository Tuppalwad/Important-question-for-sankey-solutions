def two_sum(l,target):
    i=0 
    j=len(l)-1
    while(i<len(l) and j>=0):
        if l[i]+l[j]==target:
            print(i,j)
            break
        elif target>l[i]+l[j]:
            i+=1 
        else:
            j-=1 
            
l=list(map(int,input().split()))
target=int(input())
two_sum(l,target)