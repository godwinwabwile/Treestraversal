from traversalfunctions.bfs import bfs
from traversalfunctions.dfs import dfs


if __name__== "__main__":
    graph ={"a":["b","c"], "b":["a","d"], "c":["a","e"], "d":["b"], "e":["c"]}

    visited=set()
    bfs(graph, "a")
    print(dfs(visited,graph, "a"))