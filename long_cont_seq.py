def long_cont_sum(lst):
    max_sum = lst[0]
    sum = lst[0]
    for i in lst[1:]:
        sum += i
        max_sum = max(sum,max_sum)
    print(max_sum)
        
long_cont_sum([1,2,-1,3,4,10,10,-10,-1])