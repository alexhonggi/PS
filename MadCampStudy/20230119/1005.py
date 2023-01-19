# topology sort using queue

# ref: https://velog.io/@enchantee/%EB%B0%B1%EC%A4%80-1005-Python-kvth6jbu
'''
1. 진입차수가 0인 모든 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    - 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.
'''

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split()) # 건물 수 , 건물 순서 규칙
    time = [0] + list(map(int, sys.stdin.readline().split())) # 건물들의 건설시간
    seq = [[] for _ in range(N+1)]#건설순서규칙
    inDegree=[0 for _ in range(N+1)]#진입차수
    DP=[0 for _ in range(N+1)]#해당 건물까지 걸리는 시간
 
    for _ in range(K):#건설순서규칙 저장
        a,b=map(int,sys.stdin.readline().split())
        seq[a].append(b)
        inDegree[b]+=1
 
    q = deque()
    for i in range(1,N+1):#진입차수 0인거 찾아서 큐에 넣기
        if inDegree[i]==0:
            q.append(i)
            DP[i]=time[i]
 
    while q:
        a=q.popleft()
        for i in seq[a]:
            inDegree[i]-=1#진입차수 줄이고
            DP[i]=max(DP[a]+time[i],DP[i])#DP를 이용해 건설비용 갱신
            if inDegree[i]==0:
                q.append(i)
 
 
    ans=int(sys.stdin.readline())
    print(DP[ans])