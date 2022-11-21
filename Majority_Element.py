def Find_max_friquency_element(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1 
    d=list(sorted(d.items(),key=lambda x:x[1]))
    print(d[-1][0])
l=[3,2,3]
Find_max_friquency_element(l)