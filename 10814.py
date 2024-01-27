n = int(input())
l = []

for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    l.append((a,b))
    
l.sort(key = lambda x: x[0])
for j in l:
    print(j[0], j[1])
