def quicksort(seq):
    length=len(seq)
    if length <= 1:
        return seq
    else:
        pivot=seq.pop()  #to return last val

    i_greater=[]
    i_lesser=[]

    for i in seq:
        if i > pivot:
            i_greater.append(i)
        else:
            i_lesser.append(i)
        
    return quicksort(i_lesser) + [pivot] + quicksort(i_greater)

print(quicksort([5,6,3,1,2,3,7,5,6,7,8]))