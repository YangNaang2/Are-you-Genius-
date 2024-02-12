ary = [[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    for row in range(x, x+10):
        for col in range(y, y+10):
            ary[row][col] = 1
result = 0

for i in ary:
    result += i.count(1)
print(result)
