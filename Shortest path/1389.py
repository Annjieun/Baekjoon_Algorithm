import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 친구 관계이면 1로 설정
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# 자기 자신에서 자신으로 가는 비용은 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

# 플로이드 워셜 알고리즘 수행 
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
           graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
          

min = 1000
answer = 0
for a in range(1, n + 1) :
    sum = 0
    for b in range(1, n + 1) :
        if graph[a][b] > 0 and graph[a][b] != INF :
            sum += graph[a][b]
    if sum < min :
        min = sum
        answer = a
        
print(answer)
