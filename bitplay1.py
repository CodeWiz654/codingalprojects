def firstsetbit(n):
    count = 1
    while (n):
        if (n & 1 == 1):
            break
        count += 1
        n = n >> 1
    return count

firstsetbit(64)
print(firstsetbit(64))