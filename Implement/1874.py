n = int(input())

stack = []
operator = []
falg = True
cur = 1

for _ in range(n) :
    x = int(input())
    
    while cur <= x :   
        stack.append(cur)
        operator.append('+')
        cur += 1
        
    if stack[-1] == x :   
        stack.pop()
        operator.append('-')
        
    else : 
        print("NO")
        falg = False
        break

if falg == True :
    for op in operator :
        print(op)