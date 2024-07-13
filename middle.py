def check(n : int, k : int) -> bool:
    while n:
        if n % k > 1:
            return False
        n //= k
    return True

def solve(n : int, k : int) -> int:
    s = ''
    while n:
        s += str(n % k)
        n //= k
    
    ans = 0
    for index, bit in enumerate(s):
        if bit == '1':
            ans += index
    
    return ans

n, k = map(int, input().split())

m = n
while True:
    if check(m, k):
        print(solve(m, k))
        break
    m += 1

