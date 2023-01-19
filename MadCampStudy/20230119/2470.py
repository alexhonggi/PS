# two pointer algorithm 

# input 
n = int(input())
solution = list(map(int, input().split(' ')))

# sort
solution.sort()

# twopointer setting
left = 0
right = n - 1

answer = 999999
final = []

while left < right:
    s_left = solution[left]
    s_right = solution[right]
    
    tot = s_left + s_right

    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]

    # 두 용액의 합이 0보다 작다면 왼쪽의 값을 늘려 
    if tot < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])