# source: https://www.scaler.com/topics/dfs-python/

def dfs(node, graph, visited, component):
    component.append(node) 
    visited[node] = True 

    if node in graph:
        for child in graph[node]:
            if not visited[child]: 
                dfs(child, graph, visited, component) 

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            next(file)
            graph = {}
            for line in file:
                parts = list(map(int, line.split()))
                node = parts[0]
                neighbors = parts[1:]
                graph[node] = neighbors
    except FileNotFoundError:
        print("The provided file does not exist.")
        exit()

    node_str = input("Enter the node number: ")
    try:
        node = int(node_str)
    except ValueError:
        print("Node number must be an integer.")
        exit()

    visited = {key: False for key in graph.keys()}  
    component = []
    dfs(node, graph, visited, component)
    print(f"Following is the Depth-first search: \n{component}")
