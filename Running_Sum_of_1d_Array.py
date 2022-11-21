def sum_of_running_element(l):
    ans=[l[0]]
    
    for i in l[1:]:
        ans.append(ans[-1]+i)
    print(ans)
sum_of_running_element([1,2,3,4,5])
        