n = int(input())
arr = list(map(int,input().split()))
dp = [[1,1] for i in range(n)]
index = 0
for i in range(n):
    for j in range(i+1):
        if arr[j] < arr[i]:
            temp,past = dp[j][0] + 1, j
            if dp[i][0] < temp:
                dp[i] = [temp,past]
                if temp > dp[index][0]:
                    index = i
print(dp[index][0])
result = []
while dp[index][0]!=1:
    result.append(arr[index])
    index = dp[index][1]
result.append(arr[index])
while result:
    print(result.pop(),end=" ")