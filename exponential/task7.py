n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def find_range(values, aim):
    border = 1
    last_elem = len(values) - 1
    while (border < last_elem) & (values[border] < aim):
        if values[border] == aim:
            return [border, border * 2]
        border = border * 2
        if border > last_elem:
            return [border//2, last_elem]
    return [border//2, border]

res = find_range(arr, target)
print(' '.join(map(str, res)))
