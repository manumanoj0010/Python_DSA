def partition(data, s, e):
    pivot = data[s]
    count=0
    for i in range(s+1, e+1):
        if data[i] < pivot:
            count+=1
    data[s+count], data[s] = data[s], data[s+count]
    pivot_index = s+count
    i,j= s, e
    print(data)
    while i<j:
        if data[i]<pivot:
            i+=1
        elif data[j]>= pivot:
            j+=-1
        else:
            data[i], data[j] = data[j], data[i]
            i+=1
            j+=-1
    print(data)
    return pivot_index


def quick_sort(data, s, e):
    if s>=e:
        return

    pivot_index = partition(data,s,e)
    quick_sort(data, s, pivot_index-1)
    quick_sort(data, pivot_index+1, e)
            
data = [9,3,4,8,8,82,11,11,67,34,1,30,29]
print(data)
quick_sort(data, 0, len(data)-1)
print(data)
    