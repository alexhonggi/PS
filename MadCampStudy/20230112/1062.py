# 1062
# 가르침

# Thoughts 
# 1. 필요한 갯수 숫자로만? 불가 -> 무조건 리스트 만들어야 한다
# 2. 리스트 어떻게 관리? 백트래킹

from itertools import combinations
n, k = map(int, input().split)
if k < 5:
    print(0)
else:
    k -= 5
    default_list = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z') + 1))) - default_list))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input()) - default_list:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1
        
        cnt = max(cnt, ct)
    print(cnt)