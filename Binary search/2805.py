import sys

n, m = list(map(int, sys.stdin.readline().split()))
height = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(height)

result = 0
while(start <= end) :
    total = 0
    mid = (start + end) // 2
    for h in height :
        if h > mid :
            total += h - mid
    if total < m :
        end = mid - 1
    else:
        start = mid + 1
        result = mid  
    
print(result)