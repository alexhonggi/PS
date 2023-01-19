# Union-find

'''
Union - Find 이해하기
1. 처음 각각의 원소는 연결된 정보가 없기 때문에 부모로 자기 자신을 가지고 있다.
2. find(x): x로 들어온 원소의 root 노드를 반환한다.
3. union(x, y): y의 root 노드를 x로 만드는 함수
'''

# ref: https://assaeunji.github.io/python/2020-05-05-bj4195/
'''
test_cases를 생성하고, for문을 돌린다.
parent, number를 딕셔너리형으로 받아주고
f에 친구 관계 수를 받는다.
x,y는 각 줄마다 두 명의 친구를 의미하고
만약 x와 y가 부모노드에 없다면 추가해주고 number를 1로 설정한다.
이후 union(x,y)를 통해 x←y연결 관계를 해주고
우리는 x의 최종 Root 노드의 개수를 출력하면 끝이다.
'''

# Find root node
def find(x):
    if x == parent[x]:
        return x
    else: 
        parent_x = find(parent[x])
        parent[x] = parent_x
        return parent[x]

# y의 root 노드가 x의 root 노드의 자식이 되게 만드는 함수
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] +=number[root_y]

test_cases = int(input())

for _ in range(test_cases):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x,y = input().split(" ")
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union (x,y)
        print(number[find(x)])
