import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
 
n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))
    
    
start, end = map(int, input().split())

    
def dijkstra(start) :
    q = []
    # 출발 노드로 가기 위한 최단 경로는 0으로 설정 후 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q : 
        # 최단 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재(꺼낸) 노드가 이미 처리된 적 있다면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                

dijkstra(start)

print(distance[end])
