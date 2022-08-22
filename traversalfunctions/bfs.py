import collections


def bfs(graph, root):
    '''function takes graph and root
        returns a list of all visited elements in order
    '''
    visited = []
    queue = collections.deque([root])

    while queue:
        visiting= queue.popleft()
        visited.append(visiting)
        for neighbors in graph[visiting]:
            if neighbors not in visited:
                queue.append(neighbors)
            

    print(visited)

