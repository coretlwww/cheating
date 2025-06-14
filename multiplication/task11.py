n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort()

max_product = 1
for num in arr[-k:]:
    max_product *= num

for i in range(1, k + 1, 2):
    if i <= n and (k - i) <= n:
        current_product = 1
        for num in arr[:i]:
            current_product *= num
        for num in arr[-(k - i):] if (k - i) > 0 else []:
            current_product *= num
        if current_product > max_product:
            max_product = current_product

print(max_product)