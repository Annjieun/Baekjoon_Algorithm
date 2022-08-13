x = int(input())

# DP 테이블 초기화 
d = [0] * (x+1)

# DP (Bottom-Up)
for i in range(2, x+1) :  # d[1] = 0 이므로 2부터 x까지
    # 현재의 수에서 1을 빼는 경우 (뒤에 +1은 연산 횟수를 세는 것)
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
        
print(d[x])