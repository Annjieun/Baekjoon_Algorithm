N = int(input())   
R = list(map(int, input().split()))   
C = list(map(int, input().split()))   

result = 0 
min_c = C[0]   

for i in range(len(C)-1) :
    if C[i] < min_c :
        min_c = C[i]
    result += min_c * R[i]
    
print(result)
