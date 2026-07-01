from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited
