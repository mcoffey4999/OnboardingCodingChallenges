ans = 2
start1 = 1
start2 = 2
initRes = 0
while start2 <= 4000000:
    print(ans)
    initRes = start1 + start2
    start1 = start2
    start2 = initRes
    if start2%2==0:
        ans += start2
print(ans)
