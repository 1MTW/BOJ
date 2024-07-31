from collections import deque
dp = deque([1,2])
n = int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    for i in range(2,n):
        temp = dp.popleft()
        dp.append((temp + dp[-1])%15746)
    print(dp[-1])