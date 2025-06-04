n = int(input())
arr = list(map(int, input().split()))
target = int(input())

def find_position(values, aim):
    left = 0
    right = len(values) - 1
    if aim < values[left]:
        return left
    if aim > values[right]:
        return right + 1
    while left <= right:
        middle = (left + right) // 2
        if left == right:
            if aim > values[right]:
                return right + 1
            else:
                return right
        else:
            if aim == values[middle]:
                return middle
            if aim < values[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return None

res = find_position(arr, target)
print(str(res))
