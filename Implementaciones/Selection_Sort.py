def selection_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a) - 1):
            if a[i] > a[j+1]:
                a[i], a[j+1] = a[j +1], a[i]

    return a

print(selection_sort([2, 4, 1]))