def move(l):
    None_zero=[]
    zero=[]
    for i in l:
        if i==0:
            zero.append(i)
        else:
            None_zero.append(i)
    return None_zero+zero

l=list(map(int,input().split()))
print(move(l))