import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
item = list(map(int, input().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0
            
for _ in range(r) :
    # A에서 B로 가는 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                

max = 0
for a in range(1, n + 1) :
    sum = 0
    for b in range(1, n + 1) :
        if graph[a][b] <= m :
            sum += item[b-1]
    if sum > max :
        max = sum
        
print(max)
