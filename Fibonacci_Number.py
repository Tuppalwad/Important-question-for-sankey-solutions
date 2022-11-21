def fibonacci_number(num):
    if num==0:
        return 0 
    elif num==1:
        return 1 
    else:
        l=[0,1]
        for i in range(num):
            l.append(l[-1]+l[-2])
        return l[num]
n=int(input())
print(fibonacci_number(n))