n = int(input())
people = list(map(int, input().split()))

people.sort()    

fsum = 0
result = 0

for i in range(n) :
    if i != 0 :
        fsum += people[i-1]    
        
    result += fsum + people[i]
    
    
print(result)



    