n = int(input())
arr = list(map(int, input().split()))

def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    left = []
    right = []
    middle = []

    for x in values:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)

res = quick_sort(arr)
print(' '.join(map(str, res)))