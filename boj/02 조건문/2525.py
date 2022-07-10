# 오븐 시계

A, B = map(int, input().split())
C = int(input())

def HM2min(H, M):
    m = H * 60 + M
    oneday = 24 * 60
    if m >= oneday:
        _, m = divmod(m, oneday)
    
    return m

def m2HM(m):
    H, M = divmod(m, 60)
    if H >= 24:
        _, H = divmod(H, 24)
        
    return H, M

def solution(A, B, C):
    m = HM2min(A, B)
    m += C
    H, M = m2HM(m)

    print(f'{H} {M}')

solution(A, B, C)




