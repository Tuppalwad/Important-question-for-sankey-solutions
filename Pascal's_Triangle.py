
def pascal_triangle(n):
    l=[[1],[1,1]]
    newl=[]
    for i in range(n):
        k=l[-1]
        for j in range(len(k)-1):
            newl.append(k[j]+ k[j+1])
        l.append([1]+newl+[1])
        newl=[]
    print(l[:n])
n=int(input())
pascal_triangle(n)