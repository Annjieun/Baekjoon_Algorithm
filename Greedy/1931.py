n = int(input())
meetings = [[0] * 2 for i in range(n)]

for i in range(n) :
    meetings[i] = tuple(map(int, input().split()))

meetings.sort(key=lambda x:(x[1], x[0])) 
    
count = 0
cur_time = 0

#print(meetings)

for meet in meetings : 
    if (cur_time <= meet[0]) :   
        cur_time = meet[1]       
        count += 1

print(count)
