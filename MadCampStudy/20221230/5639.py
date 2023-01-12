import sys
sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(start, end):
    if start > end:
        return
    root = end + 1
    for i in range(start + 1, end + 1):
        if num_list[start] < num_list[i]:
            root = i
            break
    
    postorder(start + 1, root - 1)
    postorder(root, end)
    print(num_list[start])

postorder(0, len(num_list) - 1)
