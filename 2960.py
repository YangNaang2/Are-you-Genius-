n, k = map(int, input().split())
li = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if li[i] == False:
        for j in range(i, n+1, i):
            if li[j] == False:
                li[j] = True
                cnt += 1
                if cnt == k:
                    print(j)
