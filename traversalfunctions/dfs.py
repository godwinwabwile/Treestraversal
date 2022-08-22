
def dfs(visited,graph, root):
    '''
    function takes an empty set, graph, and rootnode
    reruns a set of visited nodes                             
    '''
    if root not in visited:
        visited.add(root)
        for neighbors in graph[root]:
                dfs(visited, graph, neighbors)
    
    return visited