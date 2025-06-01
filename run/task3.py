n = int(input())
results = list(map(int, input().split()))

def find_best_result(values):
    best_res = max(values)
    return best_res

res = find_best_result(results)
print(str(res))
