# 더하기 사이클

# from functools import lru_cache
import sys

# N = input()
N = sys.stdin.read().rstrip()

# @lru_cache()
def get_next(N: int) -> str:
    a, b = 0, 0
    
    if N < 10:
        a = 0
        b = N
    else:
        a = N // 10
        b = N % 10

    res =  a + b
    last = res % 10

    new_num = b * 10 + last

    return new_num

N = int(N)
new_N = get_next(N)
if N == new_N:
    print(1)
else:
    counter = 1
    while 1:
        # print(new_N)
        if N != new_N:
            new_N = get_next(new_N)
            counter += 1
        else:
            print(counter)
            break
    