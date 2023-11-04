def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    if node in graph:
        for child in graph[node]:
            if not visited[child]:  # Check whether the node is visited or not
                dfs(child, graph, visited, component)  # Call the dfs recursively

if __name__ == "__main__":
    graph_file_path = "src/graph-test-100.txt"

    graph = {}
    with open(graph_file_path, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            parts = list(map(int, line.split()))
            node = parts[0]
            neighbors = parts[1:]
            graph[node] = neighbors

    node = 2  # root node
    visited = {key: False for key in graph.keys()}  # Initialize visited dictionary
    component = []
    dfs(node, graph, visited, component)
    print(f"Following is the Depth-first search: {component}")  # Print the answer
