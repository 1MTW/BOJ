from collections import deque
dp = deque([0,1])
n = int(input())
if n==0:
    print(0)
    print(dp[0])
elif n>=1:
    print(1)
    for i in range(2,n+1):
        temp = dp.popleft()
        dp.append((temp + dp[0])%1000000000)
    print(dp[-1])
else:
    for i in range(abs(n)):
        temp = dp.pop()
        temp = temp - dp[0]
        if temp<0:
            dp.appendleft((-1)*(abs(temp)%1000000000))
        else:
            dp.appendleft((temp)%1000000000)
    if dp[0]==0:
        print(0)
        print(0)
    elif dp[0]>=1:
        print(1)
        print(dp[0])
    else:
        print(-1)
        print(abs(dp[0]))