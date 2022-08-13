import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자신으로 가는 비용은 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0
            
for _ in range(m) :
    # A에서 B로 가는 비용은 C
    a, b, c = map(int, input().split())
    # 입력받은 비용이 더 작다면 입력값으로 설정
    if graph[a][b] > c :
        graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            

for a in range(1, n + 1) :
     for b in range(1, n + 1) :
         if graph[a][b] == INF :
             print("0", end=" ")
         else :
             print(graph[a][b], end=" ")         
     print()
