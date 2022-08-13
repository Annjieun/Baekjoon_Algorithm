import sys

n = int(input())
amount = list(map(int, sys.stdin.readline().split()))
m = int(input())

start = 0
end = max(amount)

while(start <= end) :
    total = 0
    mid = (start + end) // 2
    for a in amount :
        if a > mid :
            total += mid
        else :
            total += a
    if total < m :
        start = mid + 1
    else :
        end = mid - 1
        
print(end)