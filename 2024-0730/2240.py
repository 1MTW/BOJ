def make_dp(origin,arr,w): # 문제는 1번 나무에서 시작하지만 2번 나무에서 시작할 경우도 고려하고 싶어서 origin을 parameter로 추가함
    dp = [[0]*(w+1) for _ in range(len(arr))]
    for i in range(1,len(arr)):
        for j in range(min(i+1,w+1)):
            if arr[i]==origin:
                if j%2==0:
                    if j!=0: 
                        dp[i][j] = max(dp[i-1][j] + 1, dp[i-1][j-1] + 1)
                    else:
                        dp[i][0] = dp[i-1][0] + 1
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                if j%2==0: # 못잡는 상황
                    dp[i][j] = dp[i-1][j]
                else: # 잡을 수 있는 상황
                    dp[i][j] = max(dp[i-1][j] + 1, dp[i-1][j-1] + 1)
    return max(dp[-1])

t,w = map(int,input().split())
arr = [0]
for _ in range(t):
    arr.append(int(input()))
print(make_dp(1,arr,w))