def read_edges(n, m):
    edges = []
    max_node = -1
    for _ in range(m):
        parts = input().strip().split()
        if len(parts) < 2:
            print("Invalid edge line; expected two integers. Skipping.")
            continue
        u = int(parts[0])
        v = int(parts[1])
        edges.append((u, v))
        if u > max_node: max_node = u
        if v > max_node: max_node = v

    if max_node >= n:
        converted = []
        for u, v in edges:
            if u <= 0 or v <= 0:
                raise ValueError("Node indices look invalid for 1-based input.")
            converted.append((u - 1, v - 1))
        edges = converted

    return edges

def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        if 0 <= u < n and 0 <= v < n:
            graph[u].append(v)
            graph[v].append(u)
        else:
            print(f"Warning: ignoring out-of-range edge ({u},{v})")
    return graph

def dfs_cycle(node, parent, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs_cycle(neighbor, node, visited, graph):
                return True
        elif neighbor != parent:
            return True
    return False

def has_cycle_undirected(graph):
    n = len(graph)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs_cycle(i, -1, visited, graph):
                return True
    return False

def solve_graph_cycle():
    n = int(input("Enter number of nodes: ").strip())
    m = int(input("Enter number of edges: ").strip())
    print("Enter edges (one per line) as 'u v' (nodes can be 0-based OR 1-based):")
    edges = read_edges(n, m)
    graph = build_graph(n, edges)
    print("Cycle found?", has_cycle_undirected(graph))
if __name__ == "__main__":
    solve_graph_cycle()

