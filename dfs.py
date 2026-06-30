def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(graph, neighbour, visited)
    return visited
