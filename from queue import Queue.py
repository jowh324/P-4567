from queue import Queue

# 너비 우선 탐색 (BFS)
def BFS_AL(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    result = []
    while not Q.empty():
        s = Q.get()
        result.append(vtx[s])  # 정점 출력 대신 결과에 저장
        for v in aList[s]:
            if not visited[v]:
                Q.put(v)
                visited[v] = True
    return result

# 깊이 우선 탐색 (DFS)
def DFS_AL(vtx, aList, s, visited=None, result=None):
    if visited is None:
        visited = [False] * len(vtx)
    if result is None:
        result = []
    visited[s] = True
    result.append(vtx[s])  # 정점 출력 대신 결과에 저장
    for v in aList[s]:
        if not visited[v]:
            DFS_AL(vtx, aList, v, visited, result)
    return result

# 연결 성분 계산
def connected_components(vtx, aList):
    n = len(vtx)
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            component = BFS_AL(vtx, aList, i)  # BFS로 구성 요소 찾기
            components.append(component)
            for vertex in component:
                visited[vtx.index(vertex)] = True
    return components

# 스패닝 트리 계산
def spanning_tree(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    edges = []

    def dfs_tree(u):
        visited[u] = True
        for v in aList[u]:
            if not visited[v]:
                edges.append((vtx[u], vtx[v]))
                dfs_tree(v)

    dfs_tree(s)
    return edges


# 테스트용 그래프 데이터
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
aList = [[1, 2],      # 'A'의 인접정점 인덱스
         [0, 3],      # 'B'의 인접정점 인덱스
         [0, 3, 4],   # 'C'
         [1, 2, 5],   # 'D'
         [2, 6, 7],   # 'E'
         [3],         # 'F'
         [4, 7],      # 'G'
         [4, 6]]      # 'H'

# BFS 실행
print('BFS_AL(출발:A): ', end="")
print(" - ".join(BFS_AL(vtx, aList, 0)))

# DFS 실행
print('DFS_AL(출발:A): ', end="")
print(" - ".join(DFS_AL(vtx, aList, 0)))

# 연결 성분 출력
components = connected_components(vtx, aList)
print("Connected Components (BFS):")
for component in components:
    print(" - ".join(component))

# 스패닝 트리 출력
spanning_tree_edges = spanning_tree(vtx, aList, 0)
print("Spanning Tree Edges:")
for edge in spanning_tree_edges:
    print(f"{edge[0]} - {edge[1]}")