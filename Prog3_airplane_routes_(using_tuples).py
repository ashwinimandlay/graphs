# airplane routes (using tuples)
# if direct tuples are passed then it takes more time
# due to for loop running to check every case
class Graph:
    def __init__(self, routes_list):
        self.routes_list = routes_list
        self.departure_locations = [x[0] for x in routes_list]

    def get_route(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.departure_locations:
            return []

        paths = []
        for depart, arrival in self.routes_list:
            if depart is start:
                if arrival not in path:
                    new_path = self.get_route(arrival, end, path)
                    for p in new_path:
                        paths.append(p)

        return paths


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
print(route_graph.get_route(start, end))
