string = input()
arr = [a for a in string]

def find_element(sequence):
    elements = dict()
    count = 0

    for elem in sequence:
        if elem in elements:
            count += 1
        else:
            count = 1
        elements[elem] = count

    return max(elements.values())

res = find_element(arr)
print(str(res))
