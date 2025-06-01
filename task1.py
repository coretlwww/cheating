#with open("input1.txt", "r") as file:
#    n = file.readline().strip()
#    values = file.readline().strip().split(" ")

#marks = []
#for value in values:
#    mark = int(value)
#    marks.append(mark)

n = int(input())
marks = list(map(int, input().split()))

def change_zeroes(arr):
    left = 0
    right = len(arr) - 1
    while left != right:
        if arr[left] == 0:
            arr.append(arr[left])
            arr.remove(arr[left])
        left += 1
    return arr
res = change_zeroes(marks)
print(' '.join(map(str, res)))

