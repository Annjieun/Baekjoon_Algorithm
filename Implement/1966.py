from collections import deque

TC = int(input())  

for test in range(TC) :
    
    N, M = map(int, input().split())
    # 문서의 중요도   
    queue = deque(list(map(int, input().split())))  
    
    count = 0
    
    while queue :
        maximum = max(queue)
        pop = queue.popleft()
        M -= 1

        if pop == maximum :  
            count += 1 
            if M == -1 :
                print(count)
                break
        else :
            queue.append(pop)
            # 원하는 문서 위치를 재배치하기 위해 M 조정   
            if M == -1 :    
                M = len(queue) - 1