n = int(input())
digits = list(map(int, input().split()))

def find_min_dist(arr):
    dist = {}
    for i in range(len(arr) - 1):
        dist[abs(arr[i]-arr[i+1])] = [arr[i], arr[i+1]]
    min_dist = min(dist)
    return dist[min_dist]


res = find_min_dist(digits)
print(' '.join(map(str, res)))