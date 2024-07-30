n = int(input())
arr = [0] + list(map(int,input().split()))
dp = [arr[0],arr[1]]
for i in range(2,n+1):
    temp = 0
    for j in range(1,(i//2)+1):
        if temp < dp[j] + dp[-j]:
            temp = dp[j] + dp[-j]
    dp.append(max(temp,arr[i]))
print(dp[-1])