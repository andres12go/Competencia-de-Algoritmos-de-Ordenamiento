from Insertion_Sort import insertion_sort

def shell_sort(a):
    h = 1
    while h < len(a): 
        h = 3*h + 1

    while h > 0:
        h = h//3
        for i in range(0, h):
            a[i:len(a) + 1:h] = insertion_sort(a[i:len(a)+1:h])

    return a

print(shell_sort([2, 4, 1]))