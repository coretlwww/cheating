n = int(input())
elements = list(map(int, input().split()))
element = int(input())

def delete_mistake(values, mistake):
    while mistake in values:
        values.remove(mistake)
    return values

res = delete_mistake(elements, element)
print(' '.join(map(str, res)))