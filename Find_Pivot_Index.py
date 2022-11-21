def get_pivot_element_position(l):
    
    for i in range(len(l)):
        if sum(l[:i])==sum(l[i+1:]):
            return i 
l=list(map(int,input().split()))
print(get_pivot_element_position(l))