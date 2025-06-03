n = int(input())
containers = list(map(int, input().split()))

def find_last_even(arr):
    even_containers = []
    for digit in arr:
        if digit % 2 == 0:
            even_containers.append(digit)
    if len(even_containers) == 0:
        return -1
    else:
        return even_containers[-1]

res = find_last_even(containers)
print(str(res))
