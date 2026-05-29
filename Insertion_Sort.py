def insertion_sort(a):
    for i in range(1, len(a)):
        for k in range(i, 0, -1):
            if a[k] < a[k-1]:
                a[k], a[k-1] = a[k-1], a[k]
            else:
                break
    return a
if __name__ == '__main__':
    print(insertion_sort([2, 4, 1]))