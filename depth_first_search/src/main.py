class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adjacency_list[source].append(destination)

    def forward_star(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]

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

    start_node = 2  # root node
    visited = {key: False for key in graph.keys()}  # Initialize visited dictionary
    component = []
    dfs(start_node, graph, visited, component)
    print(f"Following is the Depth-first search: {component}")
