def find_squre_and_sort(l):
    Newl=[]
    for i in l:
        Newl.append(i**2)
    Newl.sort()
    return Newl
l=list(map(int,input().split()))
print(find_squre_and_sort(l))