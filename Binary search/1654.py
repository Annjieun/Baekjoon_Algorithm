import sys

n, m = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(n)]
    
start = 1
end = max(line)

result = 0
while(start <= end) :
    cnt = 0
    mid = (start + end) // 2
    for i in line :
        cnt +=  i // mid
    if cnt < m :
        end = mid - 1
    else :
        start = mid + 1
        result = mid
        
print(result)