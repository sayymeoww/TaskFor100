def check(n : int, k : int) -> bool:
    while n:
        if n % k > 1:
            return False
        n //= k
    return True

n, k = map(int, input().split())
cnt = 0 # счетчик найденных чисел

m = n
while cnt < 10:
    if check(m, 3):
        cnt += 1
        print(m)
    m += 1

    