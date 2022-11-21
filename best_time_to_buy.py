def best_time_to_buy(l): 
    left=0
    right=1 
    max_profit=0 
    k=[]
    while right<len(l):
        newlMax=l[right]-l[left]
        if l[left]<l[right]:
            max_profit=max(max_profit,newlMax)
            k.append(max_profit)
        else:
            left=right
        right+=1 
    return max_profit,k

l=list(map(int,input().split()))
print(best_time_to_buy(l))