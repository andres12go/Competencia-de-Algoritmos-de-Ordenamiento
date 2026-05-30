def bubble_sort(a):
    for i in range(0, len(a)):
        #Detects if the element was already swapped
        swapped = False
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

print(bubble_sort([2, 4, 1]))
