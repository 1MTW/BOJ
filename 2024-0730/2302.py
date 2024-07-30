dp = [0,1,2]
while len(dp)<41:
    dp.append(dp[-1] + dp[-2])
n = int(input())
m = int(input())
arr = []
progress = 1
for i in range(m):
    k = int(input())
    if progress < k:
        arr.append(dp[k-progress])
    progress = k+1
arr.append(dp[n-progress+1])
result = 1
for item in arr:
    if item!=0:
        result = result * item
print(result)
