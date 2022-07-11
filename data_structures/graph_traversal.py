class Graph:

    def __init__(self):
        self.nodes = {}

    def add_edge(self, node1, node2):
        if node1 not in self.nodes.keys():
            self.nodes[node1] = set()
        self.nodes[node1].add(node2)


def graph_search(graph, first_node_str, breadht_first=True):
    if first_node_str not in graph.nodes.keys():
            print(f'{first_node_str} not in graph!')
        print(graph.nodes)
        return -1

    stack = []
    visited = set()
    stack.append(first_node_str)

    while len(stack) > 0:
        top = stack.pop() if breadht_first else stack.pop(0)
        if top not in visited:
            visited.add(top)
            print(top)

        for neighbor in graph.nodes[top]:
            if neighbor not in visited:
                stack.append(neighbor)


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('A', 'E')
graph.add_edge('A', 'F')
graph.add_edge('A', 'G')
graph.add_edge('B', 'A')
graph.add_edge('B', 'C')
graph.add_edge('B', 'G')
graph.add_edge('C', 'A')
graph.add_edge('C', 'B')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')
graph.add_edge('D', 'C')
graph.add_edge('D', 'E')
graph.add_edge('E', 'A')
graph.add_edge('E', 'D')
graph.add_edge('E', 'F')
graph.add_edge('F', 'A')
graph.add_edge('F', 'E')
graph.add_edge('F', 'H')
graph.add_edge('G', 'A')
graph.add_edge('G', 'B')
graph.add_edge('G', 'H')
graph.add_edge('H', 'F')
graph.add_edge('H', 'G')

graph_search(graph, 'A', breadht_first=False)