def heap_sort (a): 
    n = len(a)
    #Heapify
    for i in range(n//2 - 1, -1, -1):
        sink(a, i, n)

    #Sort down
    for j in range(n):
        a[0], a[n - 1- j] = a[n - 1 - j], a[0]
        sink(a, 0, n - 1 - j)

    return a

def sink(a, i, n):
    #Left child
    lc = 2*i + 1
    if lc >= n: 
        return

    #Right child
    rc = 2*i + 2

    #Defining the maximum child
    if rc >= n:
        mc = lc
    elif a[lc] > a[rc]:
        mc = lc
    else:
        mc = rc

    #If it's in min-heap order:
    if a[i] >= a[mc]:
        return
    else:
        a[i], a[mc] = a[mc], a[i]
    
    sink(a, mc, n)

print(heap_sort([2, 4, 1]))