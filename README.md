# Repository Documentation

This repository contains files and code related to graph operations. Below is an overview of the files and their contents:

## Files

1. `dfs.py` - This file contains a Python script for performing Depth-First Search (DFS) on a graph. It reads graph data from a user-specified file, and then allows the user to specify a starting node for DFS. It prints the DFS traversal result.

2. `graph_operations.py` - This file defines a `DirectedGraph` class that provides various operations on a directed graph. It includes methods for adding vertices, adding edges, calculating in-degree and out-degree, and finding successors and predecessors of a vertex.

3. `graph-test-100.txt` - This file represents a graph in a text format with two columns, indicating the edges of the graph.

4. `graph-test-50000.txt` - This file is another representation of a graph in a text format with two columns.

## Contents of `dfs.py`

The `dfs.py` script includes the following functions:

- `dfs(node, graph, visited, component)`: This function performs Depth-First Search on the given graph.
- `main()`: The main section of the script reads graph data, takes user input for the starting node, and prints the DFS traversal.

## Contents of `graph_operations.py`

The `graph_operations.py` script includes the `DirectedGraph` class with the following methods:

- `add_vertex(vertex)`: Adds a new vertex to the graph.
- `add_edge(source, destination)`: Adds an edge between two vertices.
- `forward_star(vertex)`: Returns the list of successor vertices of a given vertex.
- `reverse_star(vertex)`: Returns the list of predecessor vertices of a given vertex.
- `in_degree(vertex)`: Calculates the in-degree of a vertex.
- `out_degree(vertex)`: Calculates the out-degree of a vertex.
- Other helper functions for file validation and reading graph data.

## How to Use

To use these scripts, follow these steps:

1. Run the `dfs.py` script by providing the name of a file containing graph data. It will prompt you to enter a starting node, and then it will print the DFS traversal result.

2. Run the `dfs.py` script by providing the name of a file containing graph data. It will prompt you to enter a starting node, and then it will print the analysis results.