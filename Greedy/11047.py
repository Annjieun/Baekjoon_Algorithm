n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

count = 0

for coin in reversed(coins) :
        count += k // coin
        k %= coin
    
print(count)


    
