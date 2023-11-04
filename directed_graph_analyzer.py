import os

class DirectedGraph:
    
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a new vertex to the adjacency list if it doesn't exist. 
        
        Args:
            vertex (int): The vertex to be read from the file.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination):
        """Add a source vertex to the adjacency list and append its corresponding destination, indicating the direction of the relationship for this pair of vertices.

        Args:
            source (int): The vertex from which the edge originates.
            destination (int): The vertex to which the edge points.
        """
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adjacency_list[source].append(destination)

    def forward_star(self, vertex):
        """Receive a vertex from the user and check if it exists in the adjacency list. If the vertex is present in the list, return a list of all successor neighbors related to this vertex.

        Args:
            vertex (int): An integer value entered by the user.

        Returns:
            list: Returns a list containing the successors of the input vertex.
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]

    def reverse_star(self, vertex):
        """Check if there is an edge that goes from the vertex of interest (parameter) to the iterating vertex. Append the value of vertex v to the list of predecessors.

        Args:
            vertex (int): The vertex of interest entered by the user.

        Returns:
            list: A list of predecessors for the input vertex.
        """
        reverse_star = []
        for v, neighbors in self.adjacency_list.items():
            if vertex in neighbors:
                reverse_star.append(v)
        
        return reverse_star

    def in_degree(self, vertex):
        """Receive the vertex and calculate the number of elements with edges directed towards it.
        
        Args:
            vertex (int): The vertex entered by the user.

        Returns:
            int: Number of elements contained.
        """
        if vertex in self.adjacency_list:
            degree = 0
            for v in self.adjacency_list:
                if vertex in self.adjacency_list[v]:
                    degree += 1
            return degree

    def out_degree(self, vertex):
        """Calculate the number of elements in the adjacency list of a vertex.

        Args:
            vertex (int): The vertex entered by the user.

        Returns:
            int: The number of elements contained in the adjacency list of the vertex.
        """
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])

def validate_file_name(file_name):
    """Validate the file name and return 'False' for two cases:
    1st case: the user doesn't enter any value in the input field.
    2nd case: the user enters a name that doesn't correspond to the files in the directory.

    Args:
        file_name (string): The file name entered by the user.

    Returns:
        bool: Returns True if the name is valid. Returns False if the name falls into the two cases described above.
    """
    if not file_name:
        print("The file name cannot be empty.")
        return False
    if not os.path.isfile(file_name):
        print(f"The file '{file_name}' was not found.")
        return False
    return True

def read_graph_from_file(file_name):
    """The method opens the file, skips reading the first line, and proceeds to the next lines of the file.

    Args:
        file_name (string): The file name entered by the user.

    Returns:
        graph: The graph as read from the file (excluding the first line).
    """
    graph = DirectedGraph()
    
    with open(file_name, 'r') as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue
            clean_data(line, graph)
    return graph

def clean_data(file_line, graph):
    """Remove whitespace from the last line read. The remaining data is separated into two variables: the source and destination vertices of the edge. Convert the values to integers and add these variables to the graph after conversion.

    Args:
        file_line (string): The complete line read from the file, including whitespace.
        graph: The graph representation in its current state.
    """
    source, destination = file_line.strip().split()
    source = int(source)
    destination = int(destination)
    graph.add_edge(source, destination)

def print_out_degree(vertex_num): 
    """Print the out-degree of the vertex entered by the user.

    Args:
        vertex_num (int): The input vertex.
    """
    print(f"I) Out-degree of {vertex_num}: {my_graph.out_degree(vertex_num)}")

def print_in_degree(vertex_num): 
    """Print the in-degree of the vertex entered by the user.

    Args:
        vertex_num (int): The input vertex.
    """
    print(f"II) In-degree of {vertex_num}: {my_graph.in_degree(vertex_num)}")

def print_successors(vertex_num):
    """Print the successors of the vertex entered by the user.

    Args:
        vertex_num (int): The input vertex.
    """
    print(f"III) Set of successors of {vertex_num}:\n\t{my_graph.forward_star(vertex_num)}")

def print_predecessors(vertex_num):
    """Print the predecessors of the vertex entered by the user.

    Args:
        vertex_num (int): The input vertex.
    """
    print(f"IV) Set of predecessors of {vertex_num}:\n\t{my_graph.reverse_star(vertex_num)}")

if __name__ == "__main__":
    while True:
        file_name = input("Enter the file name: ")
        if validate_file_name(file_name):
            my_graph = read_graph_from_file(file_name)                
            while True:
                entry = input("Vertex number: ")
                try:
                    vertex = int(entry)
                    break
                except ValueError:
                    print("Please enter a valid integer number.")
                    
            print("\n## OUTPUT")
            print_out_degree(vertex)
            print_in_degree(vertex)
            print_successors(vertex)
            print_predecessors(vertex)       
            
            break
