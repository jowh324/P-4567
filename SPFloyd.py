# 코드 11.16: Floyd 알고리즘
INF = 9999
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (A[i][j] == INF) :
                print(" INF ", end='')
            else :
                print("%4d "%A[i][j], end='')
        print("");

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)         # 정점의 개수
    parent=[[-1 if i !=j and adj[i][j]==INF else i for j in range(vsize)]for i in range(vsize)] 
    A = list(adj)			    # 2차원 배열(리스트의 리스트)의 복사
    for i in range(vsize) :
        A[i] = list(adj[i])

    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
                    parent[i][j]=parent[k][j]
        printA(A)
        
        
    return A,parent# 진행상황 출력용 

def reconstruct_path(start, end, parent, vertex):
    path = []
    if parent[start][end] == -1:
        return path
    while end != start:
        path.append(vertex[end])
        end = parent[start][end]
    path.append(vertex[start])
    path.reverse()
    return path
    


if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
    weight = [ [0,	    7,		INF,	INF,	3,      10,		INF],
               [7,		0,	    4,		10,	    2,	    6,	    INF],
               [INF,	4,		0,	    2,		INF,	INF,	INF],
               [INF,	10,     2,		0,      11,		9,	    4   ],
               [3,	    2,	    INF,   11,		0,      13,		5   ],
               [10,		6,	    INF,	9,      13,		0,	    INF],
               [INF,    INF,	INF,   4,		5,		INF,	0   ]]    

    print("Shortest Path By Floyd's Algorithm")
    dist, parent = shortest_path_floyd(vertex, weight)

    # 사용자 입력
    start_vertex = input("Start Vertex: ").strip()
    end_vertex = input("End Vertex: ").strip()

    if start_vertex in vertex and end_vertex in vertex:
        start_idx = vertex.index(start_vertex)
        end_idx = vertex.index(end_vertex)

        if dist[start_idx][end_idx] == INF:
            print(f"No path exists between {start_vertex} and {end_vertex}.")
        else:
            path = reconstruct_path(start_idx, end_idx, parent, vertex)
            print(f"* Shortest Path: {' -> '.join(path)}")
            print(f"* Distance of the Shortest Path: {dist[start_idx][end_idx]}")
    else:
        print("Invalid vertices. Please enter valid vertices from the graph.")