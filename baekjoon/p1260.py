
def dfs(curr_node):
    if dfs_visited[curr_node] == True:
        return
    dfs_visited[curr_node] = True
    dfs_visit_nodes.append(curr_node+1)

    for next_node, v in enumerate(graph[curr_node]):
        if graph[curr_node][next_node] == 1 and dfs_visited[next_node] == False:
            dfs(next_node)



def bfs(graph, visited, start):
    q = [start]
    visited[start-1] = True
    visit_nodes = []

    while len(q)>0:
        curr_node = q.pop(0)
        visit_nodes.append(curr_node)

        for next_node, v in enumerate(graph[curr_node-1]):
            if v == 1 and visited[next_node] == False:
                visited[next_node] = True
                q.append(next_node+1)

    return visit_nodes


if __name__ == "__main__":
    n, m, v = [int(i) for i in input().split(' ')]
    graph = [[0]*n for i in range(0, n)]
    visited = [False]*n
    dfs_visited = [False] * n
    dfs_visit_nodes = []

    for _ in range(0, m):
        n1, n2 = [int(i) for i in input().split(' ')]
        graph[n1-1][n2-1] = 1
        graph[n2-1][n1-1] = 1

    dfs(v - 1)
    for i in dfs_visit_nodes:
        print(i, end=' ')
    print()
    # bfs
    for i in bfs(graph, visited.copy(), v):
        print(i, end=' ')