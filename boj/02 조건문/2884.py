# 알람 시계

H, M = map(int, input().split())

def HM2min(H: int, M: int) -> int: 
    return H * 60 + M

def min2HM(m: int, Hmin=60) -> tuple:
    if m < 0:
        m = m + 24*Hmin
    H, M = divmod(m, Hmin)

    return (H, M)

def solution(H, M, offset=45):
    m = HM2min(H, M)
    m -= offset
    H, M = min2HM(m)

    print(f'{H} {M}')


solution(H, M)