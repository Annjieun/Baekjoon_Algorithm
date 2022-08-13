import sys
input = sys.stdin.readline

T = int(input())
N = [int(input()) for _ in range(T)]

d = [[0] * 2 for _ in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]
d[2] = [1, 1]

def fibo(x) :
    for i in range(3, x + 1) : 
        d[i][0] = d[i-1][0] + d[i-2][0]
        d[i][1] = d[i-1][1] + d[i-2][1]
    return d[x]
    
for x in N :
    fibo(x)
    print(d[x][0], d[x][1])