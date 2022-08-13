import sys

n = int(input())
solution = list(map(int, sys.stdin.readline().split()))
solution.sort()

start = 0
end = n - 1
answer = abs(solution[start] + solution[end])

s_start = start
s_end = end

while(start < end) :
    total = 0
    total = solution[start] + solution[end]
    
    if abs(total) < answer :
        answer = abs(total)
        s_start = start
        s_end = end
        if answer == 0 :
            break
    if total > 0 :
        end -= 1
    else :
        start += 1

print(solution[s_start], solution[s_end])

