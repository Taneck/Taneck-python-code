last = 0
ans = 0
n = int(input())
for i in range(0, n):
    temp = int(input())
    if temp > last:
        ans += (temp-last)
    last = temp
print(ans)
