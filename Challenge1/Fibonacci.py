ans = 2
start1 = 1
start2 = 2
initRes = 0
count = 0
while count <= 4000000:
    initRes = start1 + start2
    start1 = start2
    start2 = initRes
    count += 1
    if start2%2==0:
        ans += start2
print(ans)
