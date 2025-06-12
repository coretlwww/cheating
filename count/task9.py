n = int(input())
arr = list(map(int, input().split()))

middle_count = len(arr) // 2 + 1

def find_element(sequence):
    elements = dict()
    count = 0
    keys = list()

    for elem in sequence:
        if elem in elements:
            count += 1
        else:
            count = 1
        elements[elem] = count

    for key in elements.keys():
        if elements[key] >= middle_count:
            keys.append(key)
        else:
            keys.append(-1)

    return max(keys)

res = find_element(arr)
print(str(res))

