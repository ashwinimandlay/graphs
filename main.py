# shortest route in graph (based on min stops)
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}
        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

    def shortest_route(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph.keys():
            return []

        shortest_path = None
        for node in self.graph[start]:
            if node not in path:
                sp = self.shortest_route(node, end, path)
                if shortest_path is None:
                    shortest_path = sp
                elif len(shortest_path) > len(sp):
                    shortest_path = sp

        return shortest_path


routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto')
]
route_graph = Graph(routes)
start = 'Mumbai'
end = 'New York'
print(route_graph.shortest_route(start, end))
