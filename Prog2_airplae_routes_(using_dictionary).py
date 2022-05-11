# airplane routes (using dictionary)
'''
            -> Paris  \
Mumbai ->       |     New York -> Toronto
            -> Dubai  /
'''


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}
        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

    def get_path(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph.keys():
            return []

        lis = []

        for node in self.graph[start]:
            if node not in path:
                new_node = self.get_path(node, end, path)
                for p in new_node:
                    lis.append(p)
        return lis


# d = {
#     'Mumbai': ['Paris', 'Dubai'],
#     'Paris': ['Dubai', 'New York'],
#     'Dubai': ['New York'],
#     'New York': ['Toronto']
# }
routes = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto')
]
route_graph = Graph(routes)

# print(route_graph.graph)

start = 'Mumbai'
end = 'New York'
print(route_graph.get_path(start, end))
