def solve(n : int, k : int) -> int:
    arr = []
    while n:
        arr.append(n % k)
        n //= k
    arr.append(0)

    m = len(arr)
    for i in range(m - 1, -1, -1):
        if arr[i] > 1:
            for j in range(i + 1, m):
                if arr[j] == 0:
                    arr[j] = 1
                    for l in range(0, j):
                        arr[l] = 0
                    break
            break
        
    ans = 0
    for index, bit in enumerate(arr):
        if bit == 1:
            ans += index

    return ans

n, k = map(int, input().split())
print(solve(n, k))

