T = int(input())
N = [int(input()) for _ in range(T)]

d = [0] * 101
d[1] = 1
d[2] = 1

def pado(x) :
    for i in range(3, x + 1) :
        d[i] = d[i-3] + d[i-2]
        
    return d[x]

for x in N :
    print(pado(x))