# A+B - 7

import sys

T = int(input())
cases = sys.stdin.read().splitlines()
cases = [list(map(int, c.split())) for c in cases]

for i, case in enumerate(cases):
    print(f'Case #{i+1}: {sum(case)}')